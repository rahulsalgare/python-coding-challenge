from django.urls import path
from .views import (
    home, products, customerdetail,
    createcustomer, orderdelete
)

app_name = "front"

urlpatterns = [
    path('', home, name="home"),
    path('products/', products, name="products"),
    path('customerdetail/<pk>', customerdetail, name="customerdetail"),
    path('createcustomer', createcustomer, name="createcustomer"),
    path('orderdelete/<int:ck>/<int:ok>', orderdelete, name="orderdelete")
]
