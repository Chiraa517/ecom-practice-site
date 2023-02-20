from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


# Create your models here.


class Contry(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    address = models.TextField()
    country = models.ForeignKey(Contry, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Category")
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OrderStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default="Pending")
    quantity = models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quantity)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quantity
