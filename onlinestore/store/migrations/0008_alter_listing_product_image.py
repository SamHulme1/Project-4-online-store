# Generated by Django 3.2.16 on 2023-03-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20230314_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='product_image',
            field=models.ImageField(default='default.jpg', upload_to='product_images/'),
        ),
    ]