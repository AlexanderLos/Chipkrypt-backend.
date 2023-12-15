import requests
from django.core.management.base import BaseCommand
from api.models import Currency

class Command(BaseCommand):
    help = 'Fetches cryptocurrency data from CoinMarketCap API'

    def handle(self, *args, **kwargs):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '9fb53ddc-b153-457c-b63c-a0c5ca6cff95',
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        for crypto in data['data']:
            Currency.objects.update_or_create(
                symbol=crypto['symbol'],
                defaults={
                    'name': crypto['name'],
                    'currentRate': crypto['quote']['USD']['price']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully updated cryptocurrency data'))
