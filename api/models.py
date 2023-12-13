from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    portfolio = models.JSONField()

class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    currentRate = models.DecimalField(max_digits=10, decimal_places=2)
