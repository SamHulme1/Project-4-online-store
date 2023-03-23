# Generated by Django 3.2.16 on 2023-03-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20230318_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='catagory',
            field=models.CharField(choices=[('homeware', 'homeware'), ('electronics', 'electronics'), ('entertainment', 'entertainment'), ('clothing', 'clothing'), ('toys', 'toys'), ('health', 'health')], default='homeware', max_length=13),
        ),
        migrations.AlterField(
            model_name='listing',
            name='condition',
            field=models.CharField(choices=[('new', 'new'), ('like-new', 'like-new'), ('used', 'used'), ('non-functional', 'non-functional'), ('toys', 'toys'), ('health', 'health')], default='used', max_length=15),
        ),
    ]
