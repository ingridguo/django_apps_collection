from django.db import models
from datetime import datetime

# Create your models here.
#
class ItemsList(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=200, blank=True, null=True)
    is_bought = models.BooleanField(default=False)
    items_list = models.ForeignKey(ItemsList, on_delete=models.CASCADE, verbose_name="List of items")
   

    def __str__(self):
        return  self.name
    
    

