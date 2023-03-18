from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# create lsiting model
# lists appropriate options for the user when they list an item for sale
# listed items are sorted by the time they are listed newest first
# stock manager is used to sort listings that are availible and sold


class stockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            stock=Listing.Stock.AVALIBLE)


class Listing(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    product_image = models.ImageField(
        upload_to='product_images/', default='default.jpg')
    description = models.TextField()
    listedtime = models.DateField(auto_now_add=True)
    sellerID = models.ForeignKey(
        User, on_delete=models.CASCADE, default=User, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.99)
    quantity = models.IntegerField(default=1)

    class Stock(models.IntegerChoices):
        AVALIBLE = 1, "Avalible"
        SOLD = 2, "Sold"

    stock = models.PositiveSmallIntegerField(
        choices=Stock.choices,
        default=Stock.AVALIBLE
    )

    favourites = models.ManyToManyField(
        User, related_name="favourite", default=None, blank=True
    )

    class Condition(models.Model):
        choices = (
            ("new", "new"),
            ("like-new", "like-new"),
            ("used", "used"),
            ("non-functional", "non-functional"),
            ("toys", "toys"),
            ("health", "health"),
        )
    condition = models.CharField(
        choices=Condition.choices, default="used", max_length=15
    )

    class Catagory(models.Model):
        choices = (
            ("homeware", "homeware"),
            ("electronics", "electronics"),
            ("entertainment", "entertainment"),
            ("clothing", "clothing"),
            ("toys", "toys"),
            ("health", "health"),
        )
    catagory = models.CharField(
        choices=Catagory.choices, default="homeware", max_length=13
    )

    objects = models.Manager()
    avalible = stockManager()

    class Meta:
        ordering = ['-listedtime']
        indexes = [models.Index(fields=['-listedtime']),]

    def __str__(self):
        return self.title
