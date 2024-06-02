from django.shortcuts import render
from django.views import generic
from .models import Item

# purpose of a view is to get data from the models, 
# from the database model and 
# display those data back and forth to the HTML frontend

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html" 
    
    
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"