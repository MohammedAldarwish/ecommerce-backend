from django.urls import path
from .views import CheckoutView, StripeWebhookView


urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('webhook', StripeWebhookView.as_view()),
]