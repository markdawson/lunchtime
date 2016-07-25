from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem
from orders.forms import OrderAddMenuItemForm

def menu_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	menu_items = MenuItem.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		menu_items = menu_items.filter(category=category)
	return render(request, 
					'menu/menu_list.html',
					{'category':category,
					'categories':categories,
					'menu_items':menu_items})

def menu_detail(request, id, slug):
	menu_item = get_object_or_404(MenuItem,
									id=id,
									slug=slug,
									available=True)
	menu_item_form = OrderAddMenuItemForm()
	return render(request,'menu/menu_detail.html',
					{'menu_item': menu_item,
					'menu_item_form': menu_item_form})