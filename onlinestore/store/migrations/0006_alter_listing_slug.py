# Generated by Django 3.2.16 on 2023-03-12 10:20

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230311_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
