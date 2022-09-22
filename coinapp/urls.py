from django.urls import path
from coinapp.views import index

urlpatterns = [
    path('', index, name='index'),
]