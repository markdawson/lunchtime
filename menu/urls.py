from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.menu_list, name='menu_list'),
	url(r'^(?P<category_slug>[-\w]+)/$',
	 views.menu_list,
	 name='menu_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
	 views.menu_detail,
	 name="menu_detail")
]