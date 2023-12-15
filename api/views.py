from django.shortcuts import get_object_or_404
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os

class CurrencyList(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

class CoinMarketCapData(APIView):
    def get(self, request):
        return Response(self.fetch_cryptocurrency_data())

    def fetch_cryptocurrency_data(self):
        api_key = os.getenv('COINMARKETCAP_API_KEY')
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        parameters = {'start': '1', 'limit': '10', 'convert': 'USD'}
        headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()
        return data

class CurrencyDetails(APIView):
    def get(self, request, symbol):
        currency = get_object_or_404(Currency, symbol=symbol.upper())
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)
