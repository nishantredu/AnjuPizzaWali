from datetime import datetime
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Combos(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=122)
    price = models.IntegerField()
    # image = models.FileField()

    def __str__(self):
        return self.name


class Pizzas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=122)
    price = models.IntegerField()
    size = models.CharField(max_length=40)
    # image = models.FileField()
    def __str__(self):
        return self.name

class Beverages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    # image = models.FileField()
    def __str__(self):
        return self.name

class Featured(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=122)
    price = models.CharField(max_length=122)
    def __str__(self):
        return self.name

    
class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desr = models.TextField(max_length=300, default='Kuch extra ni chiye')
    address = models.TextField(max_length=122, default='Address Nahi Diya')
    datetime = models.DateTimeField()
    status = models.IntegerField(default=1)
    totalamount = models.CharField(max_length=25, default=1)
    productType= models.IntegerField(default=3)
    productId=models.IntegerField(default=1)
    def __str__(self):
        return str(self.orderid)

