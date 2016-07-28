from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import MenuItem
from .forms import OrderAddMenuItemForm, FilterDateForm
from .models import OrderItem
from django.core.mail import send_mail
from django import forms
import datetime


@require_POST
def order_add(request, menu_item_id):
	menu_item = get_object_or_404(MenuItem, id=menu_item_id)
	menu_item_form = OrderAddMenuItemForm(request.POST)
	if menu_item_form.is_valid():
		cd = menu_item_form.cleaned_data
		date = cd['date']
		item = MenuItem.objects.get(id=menu_item_id)
		new_order = OrderItem.objects.create(user=request.user,
								menu_item=item,
								price=item.price,
								quantity=cd['quantity'],
								date=date,
								comments=cd['comments'])
		new_order.save()
		return redirect('orders:upcoming_orders')
	else:
		return render(request,'menu/menu_detail.html',
					{'menu_item': menu_item,
					'menu_item_form': menu_item_form})

def order_remove(request, order_id):
	OrderItem.objects.get(id=order_id).delete()
	return redirect('orders:upcoming_orders')

def order_remove_all_staff_list(request, order_id):
	OrderItem.objects.get(id=order_id).delete()
	return redirect('orders:all_staff_orders')

def upcoming_orders(request):
	now = datetime.datetime.now()
	orders = OrderItem.objects.filter(user=request.user,
								date__gte=now).order_by('date')
	return render(request, 'orders/orders_list.html',
				 { "orders" : orders,
					"title_message": 'Upcoming Orders'})

def past_orders(request):
	now = datetime.datetime.now()
	orders = OrderItem.objects.filter(user=request.user,
								date__lt=now).order_by('-date')[:15]
	return render(request, 'orders/orders_list.html',
				 { "orders" : orders,
					"title_message": 'Past Orders'})

def all_staff_orders(request):
	orders = OrderItem.objects.all()
	if request.method =='POST':
		filter_date_form = FilterDateForm(request.POST)
		if filter_date_form.is_valid():
			cd = filter_date_form.cleaned_data
			orders = OrderItem.objects.filter(date__gte=cd['start_date'], date__lte=cd['end_date'])
	else:
		filter_date_form = FilterDateForm()
	return render(request, 
		'orders/all_staff_orders_list.html',
	 	{'orders':orders,
	 	'filter_date_form': filter_date_form})

def send_email(request):
	subject = 'Orders for {}'.format('date')
	message = "All the orders would be right here"
	to = 'mdawson@alueducation.com'
	send_mail(subject, message,'alueats@bplunch.alueducation.com', to)
	sent = True