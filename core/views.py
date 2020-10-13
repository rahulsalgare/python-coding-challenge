from rest_framework.decorators import api_view
from .models import Product, Customer, Cart
from .serializers import ProductSerializer, CustomerSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse

@api_view(['GET'])
def available_product_list(request):
    """
    Get only available products which are not already present in the cart of other customers.
    """
    products = Product.available_products.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({'Success':'Order Successfully Deleted'})
