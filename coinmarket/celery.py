import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinmarket.settings')

app = Celery('coinmarket')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'get_coin_data_5s': {
        'task': 'coinapp.tasks.get_coins_data',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()