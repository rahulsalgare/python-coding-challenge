from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status
from .models import Product, Customer, Cart
from .serializers import ProductSerializer, CustomerSerializer, CartSerializer


@api_view(['GET'])
def available_product_list(request):
    """
    Get only available products which are not already present
    in the cart of other customers.
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

    @action(methods=['get','post','delete'], detail=True, url_path='cart', url_name='customercart')
    def cart(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)

        if request.method == 'GET':
            customcart = customer.orders.all()
            serializer = CartSerializer(customcart, many=True, remove_fields=['customer_id'])
            return Response(serializer.data)

        elif request.method == 'POST':
            context = {'cust': pk}
            serializer = CartSerializer(user=pk, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            ordid = request.query_params.get('order_id')
            ord = get_object_or_404(Cart, pk=ordid)
            self.perform_destroy(ord)
            return Response({'Success':'Order Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        return Response(serialier.errors, status=status.HTTP_400_BAD_REQUEST)

class CartViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
