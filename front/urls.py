from django.urls import path, include
from .views import home, products, customerdetail, createcustomer, orderdelete

app_name = "front"

urlpatterns = [
    path('', home, name="home"),
    path('products/', products, name="products"),
    path('customerdetail/<pk>', customerdetail, name="customerdetail"),
    path('createcustomer', createcustomer, name="createcustomer"),
    path('orderdelete/<pk>', orderdelete, name="orderdelete" )
]
