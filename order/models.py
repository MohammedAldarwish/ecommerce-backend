from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()

class Order(models.Model):
    """
    Represents a customer's order:
    - Linked to a user who placed the order.
    - Tracks creation time and current status (pending, paid, or cancelled).
    - Acts as a container for multiple OrderItem entries representing individual products.
    """

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} - {self.user.name}"
    

class OrderItem(models.Model):
    """
    Represents a single product entry within an order:
    - Links to the specific product and its quantity.
    - Stores the product's price at the time of the order (in case prices change later).
    - Belongs to a specific Order instance.
    """
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in Order #{self.order.id}"
    
