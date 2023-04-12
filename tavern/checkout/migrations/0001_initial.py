# Generated by Django 4.2 on 2023-04-12 19:13

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profiles', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=40)),
                ('county', models.CharField(blank=True, max_length=80)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_basket', models.TextField(default='')),
                ('stripe_pid', models.TextField(default='', max_length=254)),
                ('user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='user_profiles.userinfo')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('pricing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.pricing')),
            ],
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['-created'], name='checkout_or_created_018c23_idx'),
        ),
    ]
