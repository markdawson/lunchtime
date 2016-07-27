from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^upcomingorders/$', views.upcoming_orders, name='upcoming_orders'),
	url(r'^pastorders/$', views.past_orders, name='past_orders'),
	url(r'^add/(?P<menu_item_id>\d+)/$', views.order_add, name='order_add'),
	url(r'^remove/(?P<order_id>\d+)/$', views.order_remove, name='order_remove'),
	url(r'^staff/remove/(?P<order_id>\d+)/$', views.order_remove_all_staff_list, name='order_remove_all_staff_list'),
	url(r'^allstafforders/$', views.all_staff_orders, name='all_staff_orders'),
]