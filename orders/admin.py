from django.contrib import admin
from .models import OrderItem, VendorEmail
from django.contrib.auth.models import User
import csv
import datetime
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if
			 not field.many_to_many and not field.one_to_many]
	# Write a first row with header information
	response.write(u'\ufeff'.encode('utf8'))
	writer.writerow([field.verbose_name for field in fields])
	# Write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d%m%Y')
			if isinstance(value, User) and value.first_name:
				value = value.first_name + " " + value.last_name
			data_row.append(value)
		writer.writerow(data_row)
	return response

export_to_csv.short_description = 'Export to CSV'

def totals_by_user(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if
			 not field.many_to_many and not field.one_to_many]
	# Write a first row with header information
	response.write(u'\ufeff'.encode('utf8'))
	writer.writerow([field.verbose_name for field in fields])
	# Write data rows
	all_orders = []
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d%m%Y')
			if isinstance(value, User) and value.first_name:
				value = value.first_name + " " + value.last_name
			data_row.append(value)
		all_orders.append(data_row)
	# make user sheet
	users = []
	
	for row in all_orders:
		if row[1] not in users:
			users.append(row[1])
	for user in users:
		user_price_total = 0
		user_quantity_total = 0
		for row in all_orders:
			if row[1] == user:
				# pull out values
				price = row[3]
				quantity = row[4]
				# write row
				writer.writerow(row)
				# update totals
				user_price_total += price * quantity
				user_quantity_total += quantity
		writer.writerow(['total',user, '', user_price_total, user_quantity_total])
		writer.writerow([])
		user_price_total = 0
		user_quantity_total = 0

	return response

totals_by_user.short_description = 'Export to CSV by User Totals'

def totals_by_user_only_totals(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if
			 not field.many_to_many and not field.one_to_many]
	# Write a first row with header information
	response.write(u'\ufeff'.encode('utf8'))
	writer.writerow(['Total','User', 'Price Total', 'Quantity Total'])
	# Write data rows
	all_orders = []
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d%m%Y')
			if isinstance(value, User) and value.first_name:
				value = value.first_name + " " + value.last_name
			data_row.append(value)
		all_orders.append(data_row)
	# make user sheet
	users = []
	
	for row in all_orders:
		if row[1] not in users:
			users.append(row[1])
	for user in users:
		user_price_total = 0
		user_quantity_total = 0
		for row in all_orders:
			if row[1] == user:
				# pull out values
				price = row[3]
				quantity = row[4]
				# write row
				# update totals
				user_price_total += price * quantity
				user_quantity_total += quantity
		writer.writerow(['total',user, user_price_total, user_quantity_total])
		user_price_total = 0
		user_quantity_total = 0

	return response

totals_by_user_only_totals.short_description = 'Export Only Totals to CSV'


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['user', 'menu_item', 'price', 
					'quantity', 'date', 'comments', 'created', 'updated']
	list_filter = ['user', 'date', 'menu_item', 'created']
	actions = [export_to_csv, totals_by_user, totals_by_user_only_totals]

admin.site.register(OrderItem, OrderItemAdmin)

class VenderEmailAdmin(admin.ModelAdmin):
	list_display = ['vendor_name', 'email', 'active', 'created']
	list_editable = ['active']

admin.site.register(VendorEmail, VenderEmailAdmin)