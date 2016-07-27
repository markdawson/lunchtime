from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    url(r'^menu/', include('menu.urls', namespace="menu")),
    url(r'^orders/', include('orders.urls', namespace="orders")),
    url(r'^account/', include('account.urls')),
]
