from django.db import models
from django.contrib.auth.models import User
import uuid
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    # user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date_created']

    first_name = models.CharField(max_length=200)
    last_initial = models.CharField(max_length=1)
    # phone = models.CharField(max_length=200, null=True)
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=200, null=True, unique=True)
    date_created = models.DateTimeField (auto_now_add=True, null=True)
    # profile_pic = models.ImageField(default = "default.png", null=True,blank=True,upload_to='images/')

    def __str__(self):
        return self.first_name +" "+ self.last_initial

    def get_full_name(self):
        return self.first_name + " "+ self.last_initial

class Product(models.Model):
    class Meta:
        ordering = ['-date_created']

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)


    # manufacturing_date = models.DateField()
    # expiry_date = models.DateField()
    # price = models.IntegerField(blank=True)
    # weight = models.IntegerField(blank=True)
    # country_id = models.CharField(max_length=1, null=True)
    # manufacture_id = models.CharField(max_length=4, null=True)
    # product_id = models.CharField(max_length=7)
    #
    # barcode = models.ImageField(upload_to="barcodes/", blank=True)
    #
    # def __str__(self):
    #     return self.name
    #
    # def save(self, *args, **kwargs):
    #     EAN = barcode.get_barcode_class('ean13')
    #     ean = EAN(f'{self.product_id}{self.country_id}{self.manufacture_id}', writer=ImageWriter())
    #     buffer = BytesIO()
    #     ean.write(buffer)
    #     self.barcode.save('barcode'+self.product_id+'.png', File(buffer), save=False)
    #     return super().save(*args, **kwargs)

class Cart(models.Model):
    class Meta:
        ordering = ['-date_created']

    STATUS = [
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    ]
    customer = models.ForeignKey(Customer,null=True,related_name="orders",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name
