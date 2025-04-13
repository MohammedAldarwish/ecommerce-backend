from django.contrib import admin
from .models import ProductImage, Product, Category

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)