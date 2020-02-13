from django.db import models

# Create your models here.


class Category(models.Model):
    CName = models.CharField(primary_key=True, max_length=30)

    class Meta:
        db_table = 'category'


class User(models.Model):
    Name = models.CharField(max_length=30,)
    Contact = models.CharField(max_length=15)
    Email = models.EmailField(primary_key=True, max_length=255)
    Password = models.CharField(max_length=16)

    class Meta:
        db_table = 'user'


class Product(models.Model):
    Pname = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Discription = models.CharField(max_length=255)
    Cname = models.ForeignKey(
        default=1, on_delete=models.CASCADE, to='Category')
    Image = models.ImageField(upload_to='image/', default="")

    class Meta:
        db_table = 'product'


class Cart(models.Model):
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    Email = models.ForeignKey(User, on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=50, default=1)

    class Meta:
        db_table = 'cart'

    def __init__(self, pid, Email):
        self.Email = Email
        self.P_id = pid
