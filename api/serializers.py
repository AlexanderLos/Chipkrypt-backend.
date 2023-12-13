from rest_framework import serializers
from .models import User, Currency

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'portfolio']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['currency_id', 'name', 'symbol', 'currentRate']

        