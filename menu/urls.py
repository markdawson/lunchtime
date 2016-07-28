from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.menu_list, name='menu_list'),
	url(r'^(?P<category_slug>[-\w]+)/$',
	 views.menu_list,
	 name='menu_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
	 views.menu_detail,
	 name="menu_detail"),
	url(r'^review/add/(?P<menu_item_id>\d+)/$',
	 views.menu_add_review,
	 name="menu_add_review"),
	url(r'^rating/add/(?P<menu_item_id>\d+)/$',
	 views.menu_add_rating,
	 name="menu_add_rating"),

]