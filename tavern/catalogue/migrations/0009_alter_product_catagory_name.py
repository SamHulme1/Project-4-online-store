# Generated by Django 3.2 on 2023-04-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_product_catagory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory_name',
            field=models.CharField(default='uncatagorised', max_length=200),
        ),
    ]
