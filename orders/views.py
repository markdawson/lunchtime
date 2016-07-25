from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import MenuItem
from .forms import OrderAddMenuItemForm
from .models import OrderItem
from django.db.models import Q
from django import forms
import datetime

@require_POST
def order_add(request, menu_item_id):
	menu_item = get_object_or_404(MenuItem, id=menu_item_id)
	form = OrderAddMenuItemForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		date = cd['date']
		if date < datetime.date.today():
			raise forms.ValidationError("The date cannot be in the past.")
		item = MenuItem.objects.get(id=menu_item_id)
		new_order = OrderItem.objects.create(user=request.user,
								menu_item=item,
								price=item.price,
								quantity=cd['quantity'],
								date=date)
		new_order.save()
		print('item created')
		return redirect('orders:upcoming_orders')
	else:
		raise forms.ValidationError("form not valid - unknown reason")

def order_remove(request, order_id):
	OrderItem.objects.get(id=order_id).delete()
	return redirect('orders:upcoming_orders')

def upcoming_orders(request):
	now = datetime.datetime.now()
	orders = OrderItem.objects.filter(user=request.user,
								date__gte=now).order_by('date')
	return render(request, 'orders/orders_list.html',
				 { "orders" : orders,
					"title_message": 'Upcoming Orders'})

def past_orders(request):
	now = datetime.datetime.now()
	orders = orders = OrderItem.objects.filter(user=request.user,
								date__lt=now).order_by('-date')[:15]
	return render(request, 'orders/orders_list.html',
				 { "orders" : orders,
					"title_message": 'Past Orders'})