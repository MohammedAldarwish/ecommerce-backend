from rest_framework import viewsets 
from .serializers import ProductSerializers
from .models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_category__name', 'product_name']
    permission_classes = [IsAuthenticatedOrReadOnly]
