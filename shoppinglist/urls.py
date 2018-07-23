from django.urls import path
from django.conf.urls import url

from . import views


app_name = "shoppinglist"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.get_items_list, name='items_list'),
    path('<int:list_id>/item/add/', views.add_item, name='add_item'),
    path('<int:list_id>/item/<int:id>/', views.get_item, name='item'),
    path('<int:id>/add/', views.add_items_list, name='add_items_list'),
    path('<int:id>/edit/', views.edit_items_list, name='edit_items_list'),
    path('<int:id>/delete/', views.delete_items_list, name='delete_items_list'),
    path('<int:list_id>/item/<int:id>/edit/', views.edit_item, name='edit_item'),
    path('<int:list_id>/item/<int:id>/delete/', views.delete_item, name='delete_item'),
    path('<int:list_id>/item/<int:id>/buy/', views.buy_item, name='buy_item'),
 
]