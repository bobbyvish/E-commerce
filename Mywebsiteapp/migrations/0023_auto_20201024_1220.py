# Generated by Django 2.2.3 on 2020-10-24 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mywebsiteapp', '0022_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
