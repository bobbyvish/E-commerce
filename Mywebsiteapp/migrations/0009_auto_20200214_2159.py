# Generated by Django 2.2.3 on 2020-02-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mywebsiteapp', '0008_auto_20200213_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='P_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='Quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]