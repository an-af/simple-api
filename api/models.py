# id, name, email, phone
from django.db import models

# Customer
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'customer'

# Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'