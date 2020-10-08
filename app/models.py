from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    def __str__(self):
        return self.name

class Customer(models.Model):

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username