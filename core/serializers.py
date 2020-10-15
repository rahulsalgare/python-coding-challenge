from rest_framework import serializers
from .models import Product, Customer, Cart


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class CartSerializer(serializers.ModelSerializer):

    #dynamically exclude fields for different requests
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        self.user = kwargs.pop('user', None)
        super(CartSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)


    order_id = serializers.CharField(source='id', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_id = serializers.CharField(source='product.id')
    customer_id = serializers.CharField(source='customer.id', read_only=True)
    customer_name = serializers.CharField(source='customer.get_full_name', read_only=True)

    class Meta:
        model = Cart
        fields = [
            'order_id', 'customer_id', 'customer_name',
            'product_id', 'product_name', 'date_created', 'status'
        ]

    def save(self, **kwargs):
        """
        Get the customer and product instance by their id
        and create a cart instance and save it.
        """
        cust = Customer.objects.get(id=self.user)
        prod = Product.objects.get(id=self.validated_data['product']['id'])
        status = self.validated_data['status']
        cart = Cart(customer=cust, product=prod, status=status)
        cart.save()
        return cart


class CustomerSerializer(serializers.ModelSerializer):
    # orders = CartSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_initial',
            'phone', 'email', 'date_created', 'orders'
        ]
