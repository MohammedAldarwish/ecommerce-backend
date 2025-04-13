from rest_framework import serializers
from .models import Cart, CartProduct
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price']


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']


class CartSerializers(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'products']

    def get_products(self, obj):
        cart_products = obj.cart_products.all()
        return CartProductSerializer(cart_products, many=True).data

        