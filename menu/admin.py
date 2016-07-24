from django.contrib import admin
from .models import Category, MenuItem

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'price', 'category', 'available']
	list_filter = ['available']
	list_editable = ['price', 'available']

admin.site.register(MenuItem, MenuItemAdmin)