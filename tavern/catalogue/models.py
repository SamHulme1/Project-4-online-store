from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pricing(models.Model):
    title = models.CharField(max_length=200, default="title")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=20)
    promo_image = models.ImageField(
        upload_to='promo_images/', default='default.jpg')
    description = models.TextField(default='description')
    created = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']),]

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, default="title")
    product_image = models.ImageField(
        upload_to='product_images/', default='default.jpg')
    description = models.TextField(default='description')
    created = models.DateField(auto_now_add=True)
    catagory_name = models.CharField(
        max_length=200, default="uncatagorised", null=False)
    catagory = models.ForeignKey(
        Pricing, blank=True, null=True, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(
        User, related_name="favourite", blank=True, default=None,
    )

    objects = models.Manager()

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']),]

    def __str__(self):
        return self.title
