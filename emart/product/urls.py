from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import showall

urlpatterns=[

	path('home',views.home,name='product-home'),
	path('show',views.showall, name='products')
	]