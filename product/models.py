from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=32)
    product_description = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product_stock_quantity = models.IntegerField(default=0)


    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f"image for {self.product.product_name}"