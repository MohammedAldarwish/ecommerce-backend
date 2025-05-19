from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product  

User = get_user_model()

class Cart(models.Model):
    """
    Represents a shopping cart linked to a single user:
    - Each user has one cart.
    - Tracks when the cart was created.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartProduct(models.Model):
    """
    Represents a product entry inside a cart:
    - Links a product to a cart with a specific quantity.
    - Ensures each product appears only once per cart.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['cart', 'product']

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name} in Cart"

