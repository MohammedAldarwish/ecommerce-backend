from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),


    path('api/accounts/', include('accounts.urls')),
    path('api/product/', include('product.urls')),



    path('api/cart/', include('cart.urls')),
    path('api/order/', include('order.urls'))
]
