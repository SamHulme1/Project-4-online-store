# Generated by Django 3.2 on 2023-04-20 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20230420_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='promo_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
