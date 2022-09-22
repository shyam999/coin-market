from django.urls import path
from coinapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/coin-list/', views.CoinListAPI.as_view(), name='api_coin_list')
]