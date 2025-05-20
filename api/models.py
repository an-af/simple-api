# id, name, email, phone
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'customer'