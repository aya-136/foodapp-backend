from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process_payment, name='process_payment'),
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
]
