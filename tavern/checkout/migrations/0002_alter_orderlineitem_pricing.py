# Generated by Django 3.2 on 2023-04-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_alter_product_catagory_name'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='pricing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.pricing'),
        ),
    ]
