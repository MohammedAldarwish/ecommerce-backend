from rest_framework import serializers
from .models import Product
 

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_price', 'product_description', 'product_category', 'product_stock_quantity']


    def create(self, validated_data):
        validated_data['added_by'] = self.context['request'].user
        return super().create(validated_data)