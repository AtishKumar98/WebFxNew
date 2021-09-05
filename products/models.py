from django.db import models



class Product(models.Model):
    name=models.CharField(max_length=255,default='Username..')
    type=models.CharField(max_length=244,default='Type of Product..')
    requirements=models.CharField(max_length=255,default='Requirement of products')

# Create your models here.
