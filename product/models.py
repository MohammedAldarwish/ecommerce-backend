from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    """
    Represents a product category with a unique name.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


User = get_user_model()


class Product(models.Model):
    """
    Represents a product with details:
    - Name, price, description, category, and stock quantity.
    - Tracks who added the product and timestamps for creation/update.
    """
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_stock_quantity = models.IntegerField(default=0)

    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    """
    Stores images related to a product:
    - Each image linked to one product.
    - Supports multiple images per product.
    """
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f"image for {self.product.product_name}"