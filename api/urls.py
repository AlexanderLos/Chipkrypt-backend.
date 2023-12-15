from django.urls import path
from .views import CurrencyList, CoinMarketCapData, CurrencyDetails, home

urlpatterns = [
    path('', home),
    path('currencies/', CurrencyList.as_view()),
    path('coinmarketcap-data/', CoinMarketCapData.as_view()),
    path('crypto-details/<str:symbol>/', CurrencyDetails.as_view()), 
]
