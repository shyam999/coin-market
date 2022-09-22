from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, blank=True)
    time_1h = models.CharField(max_length=50, blank=True)
    time_24h = models.CharField(max_length=50, blank=True)
    time_7d = models.CharField(max_length=50, blank=True)
    market_cap = models.CharField(max_length=50, blank=True)
    Volume_24h = models.CharField(max_length=50, blank=True)
    circulating_supply = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
