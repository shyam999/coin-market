from django.shortcuts import render



from rest_framework import generics
from coinapp.models import Coin
from .serializers import CoinSerializer


class CoinListAPI(generics.ListAPIView):
    model = Coin
    serializer_class = CoinSerializer
    queryset = Coin.objects.all()




def index(request):
    return render(request, 'index.html')