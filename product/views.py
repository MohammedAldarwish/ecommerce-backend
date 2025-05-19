from rest_framework import viewsets 
from .serializers import ProductSerializers
from .models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

class ProductViewsets(viewsets.ModelViewSet):
    """
    Manages product API endpoints:
    - Anyone can view products.
    - Only admin users can create, update, or delete products.
    - Supports filtering products by category name and product name.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_category__name', 'product_name']



    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
