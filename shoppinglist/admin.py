from django.contrib import admin

# Register your models here.
from .models import Item
from .models import ItemsList

admin.site.register(ItemsList)
admin.site.register(Item)