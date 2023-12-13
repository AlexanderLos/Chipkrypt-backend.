from django.urls import path
from .views import CurrencyList  

urlpatterns = [
    path('currencies/', CurrencyList.as_view()),
    
]
