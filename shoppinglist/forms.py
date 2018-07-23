from django import forms
from .models import ItemsList, Item

# https://github.com/rodionovsasha/ShoppingListDjango/blob/master/shoppinglist/forms.py

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'comment',)
        labels = {'name': 'Nome'}

class ItemsListForm(forms.ModelForm):
    class Meta:
        model = ItemsList
        fields = ['name']
