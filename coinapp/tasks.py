import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from celery import shared_task
from .models import Coin


@shared_task
def get_coins_data():
    options = Options()
    options.headless= True
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://coinmarketcap.com')
    for i in range(1):
        driver.execute_script("window.scrollBy(0,2500)","")
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,2500)","")
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,2500)","")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    data_set = []
    table = soup.find('table', class_='cmc-table')
    for row in table.find_all('tr'):
        try:
            data = {}
            data['name'] = row.find('div', class_='dNOTPP').find('p').text
            data['price'] = row.find('div', class_='cLgOOr').text
            data['time_1h'] = row.select_one('td:nth-of-type(5)').find('span', class_='sc-15yy2pl-0').text
            data['time_24h'] = row.select_one('td:nth-of-type(6)').find('span', class_='sc-15yy2pl-0').text
            data['time_7d'] = row.select_one('td:nth-of-type(7)').find('span', class_='sc-15yy2pl-0').text
            data['market_cap'] = row.find('p', class_='hykWbK').find('span', class_='ieFnWP').text
            data['volume_24h'] = row.find('div', class_='cRcnjD').find('p', class_='hykWbK').text
            data['circulating_supply'] = row.find('div', class_='eGQXzN').find('p', class_='kZlTnE').text
            data_set.append(data)
        except AttributeError:
            continue
    for coin in data_set:
        obj, created = Coin.objects.get_or_create(name=coin['name'])
        obj.price=coin['price']
        obj.time_1h=coin['time_1h']
        obj.time_24h=coin['time_24h']
        obj.time_7d=coin['time_7d']
        obj.market_cap=coin['market_cap']
        obj.volume_24h=coin['volume_24h']
        obj.circulating_supply=coin['circulating_supply']
        obj.save()
        
