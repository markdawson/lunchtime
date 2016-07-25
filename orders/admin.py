from django.contrib import admin
from .models import OrderItem

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['user', 'menu_item', 'price', 
					'quantity', 'date', 'created', 'updated']
	list_filter = ['user', 'date', 'menu_item', 'created']

admin.site.register(OrderItem, OrderItemAdmin)