from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('menu:menu_list_by_category', args=[self.slug])

class MenuItem(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	category = models.ForeignKey(Category,
						related_name='menu_items')
	price = models.PositiveIntegerField()
	available = models.BooleanField(default = True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('menu:menu_detail', args=[self.id, self.slug])