from django.urls import path, include
from .views import (
    ProductViewSet, CartViewSet,
    CustomerViewSet, available_product_list,
)
from rest_framework.routers import DefaultRouter

app_name = "core"

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'product', ProductViewSet)
    
urlpatterns = [
    path('', include(router.urls)),
    path('available_products', available_product_list, name='availableproducts'),
]
