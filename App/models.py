from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=300,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name
    

class PromotionProducts(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    product = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=300,null=True)
    active = models.CharField(max_length=100,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=200,null=True)
    address = models.TextField(max_length=600,null=True)
    def __str__(self):
        return self.name
        

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return self.customer.name
        

