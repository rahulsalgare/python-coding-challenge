from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    class Meta:
        ordering = ['-date_created']

    first_name = models.CharField(max_length=200)
    last_initial = models.CharField(max_length=1)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=200, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_initial

    def get_full_name(self):
        return self.first_name + " " + self.last_initial


class AvailabeProductsManager(models.Manager):
    """
    Manager to get the products that are available to add in cart.
    products which dont have relationship with cart).
    """
    def all(self):
        available = []
        for pr in Product.objects.all():
            try:
                pr.status
            except Cart.DoesNotExist:
                available.append(pr)
        return available

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    objects = models.Manager()
    available_products = AvailabeProductsManager()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name

class Cart(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]
    customer = models.ForeignKey(Customer, null=True, related_name="orders", on_delete=models.CASCADE)
    product = models.OneToOneField(Product, null=True, related_name="status", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.product.name
