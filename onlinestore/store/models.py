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
        upload_to='product_images/')
    description = models.TextField()
    listedtime = models.DateField(auto_now_add=True)
    sellerID = models.ForeignKey(
        User, on_delete=models.CASCADE,
        default=User)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.99)

    class Stock(models.IntegerChoices):
        AVALIBLE = 1, "Avalible"
        SOLD = 2, "Sold"
    stock = models.PositiveSmallIntegerField(
        choices=Stock.choices,
        default=Stock.AVALIBLE
    )

    class Condition(models.IntegerChoices):
        NEW = 1, "New"
        LNEW = 2, "Like New"
        USED = 3, "Used"
        NONF = 4, "None Functional"
    condition = models.PositiveSmallIntegerField(
        choices=Condition.choices, default=Condition.USED
    )

    class Catagory(models.IntegerChoices):
        HOMEWARE = 1, "Homeware"
        ELECTRONICS = 2, "Electronics"
        ENTERTAINMENT = 3, "Entertainment"
        CLOTHING = 4, "Clothing"
        TOYS = 5, "Toys"
        HEALTH = 6, "Health"

    catagory = models.PositiveSmallIntegerField(
        choices=Catagory.choices, default=Catagory.HOMEWARE
    )

    objects = models.Manager()
    avalible = stockManager()

    class Meta:
        ordering = ['-listedtime']
        indexes = [models.Index(fields=['-listedtime']),]

    def __str__(self):
        return self.title



