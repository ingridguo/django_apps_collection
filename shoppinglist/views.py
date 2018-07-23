from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemsList, Item
from .forms import ItemsListForm, ItemForm


# Create your views here.
def index(request):
    lists = ItemsList.objects.all()
    return render(request, 'shoppinglist/index.html', {'lists': lists})

def get_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    items = items_list.item_set.all().order_by('is_bought', 'name')
    return render(request, 'shoppinglist/items_list.html', {'list': items_list, 'items': items})

def add_items_list(request):
    if request.method == "POST":
        form = ItemsListForm(request.POST)
        if form.is_valid():
            items_list = form.save()
            urlstr = '/shoppinglist/{}/add/'.format(items_list.id)
            return redirect(urlstr)
        else:
            return render(request, 'shoppinglist/add_items_list.html',  {'form': form})
    else:
        form = ItemsListForm()
        return render(request, 'shoppinglist/add_items_list.html', {'form': form})

def edit_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    if request.method == "POST":
        form = ItemsListForm(request.POST, instance=items_list)
        if form.is_valid():
            form.save()
            urlstr = '/shoppinglist/{}/edit/'.format(id)
            return redirect(urlstr)
        else:
            return render(request, 'shoppinglist/edit_items_list.html',  {'form': form})
    else:
        form = ItemsListForm(instance=items_list)
        return render(request, 'shoppinglist/edit_items_list.html', {'form': form})

def delete_items_list(request, id):
    items_list = get_object_or_404(ItemsList, pk=id)
    items_list.delete()
    return redirect('index')

def get_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'shoppinglist/item.html', {'item': item})

def add_item(request, list_id):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.items_list = get_object_or_404(ItemsList, pk=list_id)
            item.save()
            urlstr = '/shoppinglist/{}/item/{}'.format(list_id, item.id)
            return redirect(urlstr)
        else:
            return render(request, 'shoppinglist/add_item.html',  {'form': form, 'list_id': list_id})
    else:
        form = ItemForm()
        return render(request, 'shoppinglist/add_item.html', {'form': form, 'list_id': list_id})

def edit_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            urlstr='/shoppinglist/{}/item/{}/edit/'.format(list_id, id)
            return redirect(urlstr)
        else:
            return render(request, 'shoppinglist/edit_item.html',  {'form': form, 'list_id': list_id})
    else:
        form = ItemForm(instance=item)
        return render(request, 'shoppinglist/edit_item.html', {'form': form, 'list_id': list_id})

def delete_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    urlstr='/shoppinglist/{}/delete/'.format(id)
    return redirect(urlstr)
    
def buy_item(request, list_id, id):
    item = get_object_or_404(Item, pk=id)
    item.is_bought = not item.is_bought
    item.save()
    urlstr='/shoppinglist/{}/'.format(list_id)
    return redirect(urlstr)