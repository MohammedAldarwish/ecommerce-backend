from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('product/', include('product.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('cart/', include('cart.urls')),
    path('order/', include('order.urls'))
]
