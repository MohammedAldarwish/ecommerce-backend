from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewsets

router = DefaultRouter()
router.register('', ProductViewsets)

urlpatterns = [
    path('', include(router.urls)),
]