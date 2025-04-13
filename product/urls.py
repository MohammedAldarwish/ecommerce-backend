from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewsets

router = DefaultRouter()
router.register('product', ProductViewsets)

urlpatterns = [
    path('', include(router.urls)),
]