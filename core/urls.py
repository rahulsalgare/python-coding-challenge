from django.urls import path, include
from .views import (ProductViewSet, CartViewSet, CustomerViewSet)
from rest_framework.routers import DefaultRouter

app_name = "core"

router = DefaultRouter()
router.register(r'cart', CartViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'product', ProductViewSet)

for url in router.urls:
    print(url)


urlpatterns = [
    # path('products', product_list, name='productlist'),
    # path('productdetail/<pk>', product_detail, name='productdetail'),
    # path('addproduct',add_product, name='addproduct'),
    # path('updateproduct/<int:pk>',UpdateProduct.as_view(), name='updateproduct'),
    # path('deleteproduct/<int:pk>', delete_product, name='deleteproduct'),
    # path('customers', customer_list, name='customerlist'),
    # path('customerdetail/<int:pk>', customer_detail, name='customerdetail'),
    # path('addcustomer', add_customer, name='addcustomer'),
    # path('updatecustomer/<int:pk>',UpdateCustomer.as_view(), name='updatecustomer'),
    # path('deletecustomer/<int:pk>',delete_customer, name='deletecustomer'),
    path('', include(router.urls)),
]


#  customer_list,
# customer_detail, add_customer,
# UpdateCustomer, delete_customer,
