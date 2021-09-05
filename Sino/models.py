from django.db import models

class customer(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    def __str__(self):
        return self.firstname

class Category(models.Model):
    name=models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name



# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    type=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    price=models.CharField(max_length=255,default='')
    Image_url=models.CharField( max_length=2085,default='')
    Description=models.CharField(max_length=255,default='')
    def __str__(self):
        return self.name

class Status(models.Model):
    status=models.CharField( max_length=255,default='')
    type=models.CharField(null=True, max_length=255,default='')
    def __str__(self):
        return self.status



class Order(models.Model):
    name=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    status=models.ForeignKey(Status, on_delete=models.CASCADE,null=True)
    extra=models.CharField(max_length=255)