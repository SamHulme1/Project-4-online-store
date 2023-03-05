from django.contrib import admin
from .models import CreateListing

# listing order for listings on admin site
# listings can be sorted by catagory, condition, price, sellerID and listedtime
# listings are searchable by their title, descriptions and catagories


@admin.register(CreateListing)
class CreateListingOrder(admin.ModelAdmin):
    list_display = ["title", "slug", "catagory",
                    "description", "price", "condition",
                    "sellerID", "listedtime", "stock"]
    list_filter = ["catagory", "condition", "price", "sellerID", "listedtime",
                   "stock"]
    search_fields = ["title", "description", "catagory"]
    raw_id_fields = ["sellerID"]
    ordering = ["listedtime", "stock"]
