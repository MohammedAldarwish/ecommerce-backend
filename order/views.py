from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart
from order.models import Order , OrderItem


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user).first()

        if not cart or not cart.cart_products.exists():
            return Response({'detail': 'Cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)
        
        order = Order.objects.create(user=user)

        
        for cart_product in cart.cart_products.all():
            product = cart_product.product
            quantity = cart_product.quantity

            
            if quantity > product.product_stock_quantity:
                return Response(
                    {'detail': f"Only {product.product_stock_quantity} of '{product.name}' available."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_order=product.product_price
            )

            product.product_stock_quantity -= quantity
            product.save()

        cart.cart_products.all().delete()
        return Response({'detail': 'Order placed successfully.'}, status=status.HTTP_201_CREATED)


