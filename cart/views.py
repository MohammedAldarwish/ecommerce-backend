from rest_framework import viewsets, permissions
from .models import Cart, CartProduct
from product.models import Product
from .serializers import CartSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class CartViewSet(viewsets.ModelViewSet):
    """
    Handles all cart-related API operations for authenticated users:
    - Prevents creating multiple carts per user.
    - Adds products to the user's cart, checking stock availability.
    - Allows viewing the current cart contents.
    - Updates product quantities inside the cart.
    - Removes products from the cart.
    - Uses custom actions for add/update/remove operations.
    """

    serializer_class = CartSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "You already have a cart. You can't create another one."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['post'])
    def add_product_to_cart(self, request):
        product_id = request.data.get('id')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)

        current_quantity = cart_product.quantity if not created else 0
        total_quantity = current_quantity + quantity

        if total_quantity > product.product_stock_quantity:
            return Response({
                'detail': f"Only {product.product_stock_quantity} items available."
            }, status=status.HTTP_400_BAD_REQUEST)

        cart_product.quantity = total_quantity
        cart_product.save()

        return Response({"detail": "Product added to cart."}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def view_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
    

    @action(detail=False, methods=['post'])
    def update_quantity(self, request):
        product_id = request.data.get('id')
        quantity = int(request.data.get('quantity', 1))

        if quantity < 1:
            return Response({"detail": "Quantity must be at least 1."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
            cart = Cart.objects.get(user=request.user)
            cart_product = CartProduct.objects.get(cart=cart, product=product)
            cart_product.quantity = quantity
            cart_product.save()
            return Response({"detail": "Quantity updated."})
        except (Product.DoesNotExist, Cart.DoesNotExist, CartProduct.DoesNotExist):
            return Response({"detail": "Product not found in cart."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['delete'])
    def remove_product(self, request):
        product_id = request.data.get('id')

        try:
            product = Product.objects.get(id=product_id)
            cart = Cart.objects.get(user=request.user)
            cart_product = CartProduct.objects.get(cart=cart, product=product)
            cart_product.delete()
            return Response({"detail": "Product removed from cart."})
        except (Product.DoesNotExist, Cart.DoesNotExist, CartProduct.DoesNotExist):
            return Response({"detail": "Product not found in cart."}, status=status.HTTP_404_NOT_FOUND)
