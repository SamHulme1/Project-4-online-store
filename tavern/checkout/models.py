import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from catalogue.models import Pricing
from user_profiles.models import UserInfo


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_info = models.ForeignKey(
        UserInfo, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=150, null=False, blank=True)
    last_name = models.CharField(max_length=150, null=False, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=150, null=False, blank=True)
    city = models.CharField(max_length=40, null=False, blank=True)
    county = models.CharField(max_length=80, null=False, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=True)
    country = CountryField(blank_label='Country', null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.TextField(
        max_length=254, null=False, blank=False, default='')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])]

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def calculate_order_total(self):
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery_cost = self.order_total * settings.STANDARD_DELEVERY_PERCENTAGE / 100
        self.grand_total = self.order_total + self.delivery_cost
        super().save()

    def __str__(self):
        return str(self.order_number)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    pricing = models.ForeignKey(
        Pricing, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.pricing.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order.order_number)