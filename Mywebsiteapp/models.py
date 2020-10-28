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


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


class Product(models.Model):
    Pname = models.CharField(max_length=100)
    Price = models.FloatField(max_length=100)
    Discription = models.CharField(max_length=255)
    Cname = models.ForeignKey(
        default=1, on_delete=models.CASCADE, to='Category')
    Image = models.ImageField(upload_to='image/', default="")

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.Pname


class Cart(models.Model):
    Product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    Email = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # active = models.BooleanField(default=True)
    Quantity = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'cart'


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.Price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
