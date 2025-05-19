from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart
from order.models import Order, OrderItem
import stripe
import os
from dotenv import load_dotenv

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils.decorators import method_decorator

load_dotenv()
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class CheckoutView(APIView):
    """
    Handles the checkout process for authenticated users:
    - Checks if the user has a cart with items.
    - Creates a new Order and links all cart products to it.
    - Validates that requested quantities are in stock.
    - Deducts the purchased quantity from the product stock.
    - Creates a Stripe Checkout Session and returns the payment URL to the user.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user).first()

        if not cart or not cart.cart_products.exists():
            return Response({'detail': 'Cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)

        line_items = []

        for cart_product in cart.cart_products.all():
            product = cart_product.product
            quantity = cart_product.quantity

            if quantity > product.product_stock_quantity:
                return Response(
                    {'detail': f"Only {product.product_stock_quantity} of '{product.product_name}' available."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_order=product.product_price
            )

            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': product.product_name},
                    'unit_amount': int(product.product_price * 100),  # in cents
                },
                'quantity': quantity,
            })

            product.product_stock_quantity -= quantity
            product.save()

        cart.cart_products.all().delete()

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url='https://yourdomain.com/success',  # your domain 
                cancel_url='https://yourdomain.com/cancel',    # your domain 
                metadata={'order_id': order.id}
            )
            return Response({'checkout_url': session.url}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'detail': 'Payment session failed.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(APIView):
    """
    Handles incoming Stripe webhook events:
    - Verifies the Stripe signature to ensure the request is valid.
    - If the checkout session is completed, updates the corresponding order status to 'paid'.
    - Uses the 'order_id' from the session metadata to find and update the correct Order.
    """

    def post(self, request):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
        endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError:
            return HttpResponse(status=400)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            order_id = session['metadata'].get('order_id')
            try:
                order = Order.objects.get(id=order_id)
                order.status = 'paid'  
                order.save()
            except Order.DoesNotExist:
                pass

        return HttpResponse(status=200)