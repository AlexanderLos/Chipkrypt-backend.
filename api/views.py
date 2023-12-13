from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Currency
from .serializers import CurrencySerializer

# Create your views here.
class CurrencyList(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)