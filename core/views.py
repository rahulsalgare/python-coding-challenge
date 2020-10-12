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
    products = Product.available_products.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def product_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     serializer = ProductSerializer(product, many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def add_product(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# class UpdateProduct(UpdateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_object(self):
#         obj = get_object_or_404(Product, id=self.kwargs['pk'])
#         return obj
#
#     def get_queryset(self):
#         return
#
# @api_view(['DELETE'])
# def delete_product(request, pk):
#     data = {}
#     product = get_object_or_404(Product, id=pk)
#     product.delete()
#     data['success'] = "product successfully deleted"
#     return Response(data)

# @api_view(['GET'])
# def customer_list(request):
#     customers = Customer.objects.all()
#     serializer = CustomerSerializer(customers, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def customer_detail(request, pk):
#     customer = Customer.objects.get(id=pk)
#     serializer = CustomerSerializer(customer, many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def add_customer(request):
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# class UpdateCustomer(UpdateAPIView):
#     serializer_class = CustomerSerializer
#
#     def get_object(self):
#         obj = get_object_or_404(Customer, id=self.kwargs['pk'])
#         return obj
#
#     def get_queryset(self):
#         return
#
# @api_view(['DELETE'])
# def delete_customer(request, pk):
#     data = {}
#     customer = get_object_or_404(Customer, id=pk)
#     customer.delete()
#     data['success'] = "Customer successfully deleted"
#     return Response(data)

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


    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def get_object(self):
    #     print(self.kwargs[self.lookup_field])
    #     obj = Cart.objects.filter(customer=self.kwargs[self.lookup_field])
    #     return obj
