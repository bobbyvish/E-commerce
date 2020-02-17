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
    Product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    Email = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    # Quantity = models.CharField(max_length=50, default=1)

    class Meta:
        db_table = 'cart'

    def __unicode__(self):
        return "Cart id: %s" % (self.id)

    # def __unicode__(self):
    #     return "%s" % (self.Email)

    # def add_to_cart(self, book_id):
    #     product = Product.objects.get(pk=book_id)
    #     try:
    #         preexisting_order = ProductOrder.objects.get(
    #             product_id=product, cart=self)
    #         preexisting_order.Quantity += 1
    #         preexisting_order.save()
    #     except ProductOrder.DoesNotExist:
    #         new_order = BookOrder.objects.create(
    #             product_id=product
    #             cart=self
    #             quantity=1
    #         )
    #         new_order.save()

    #         def __unicode__(self):
    #             return "%s" % (self.book_id)
