from rest_framework import serializers
from .models import Product, Customer, Cart
from phonenumber_field.serializerfields import PhoneNumberField

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['id','name','description','price']

class CartSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(source='id', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_id = serializers.CharField(source='product.id')
    customer_id = serializers.CharField(source='customer.id')
    customer_name = serializers.CharField(source='customer.get_full_name', read_only=True)

    class Meta:
        model = Cart
        fields = ['order_id','customer_id','customer_name','product_id','product_name','date_created','status']

    def save(self, **kwargs):
        if self.instance is not None:
            print("updating")
        else:
            print(self.validated_data)
            cust= Customer.objects.get(id=self.validated_data['customer']['id'])
            prod = Product.objects.get(id=self.validated_data['product']['id'])
            status = self.validated_data['status']
            cart = Cart(customer=cust,product=prod,status=status)
            cart.save()
            return cart


class CustomerSerializer(serializers.ModelSerializer):
    orders = CartSerializer(many=True, read_only=True)
    # orders = serializers.StringRelatedField(many=True)
    # orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id','first_name','last_initial','phone','email','date_created','orders']
