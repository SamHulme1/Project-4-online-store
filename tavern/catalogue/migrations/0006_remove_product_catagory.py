# Generated by Django 3.2 on 2023-04-17 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_product_pricing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catagory',
        ),
    ]
