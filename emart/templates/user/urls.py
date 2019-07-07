from . import views
from django.contrib import admin
from django.urls import path
urlpatterns=[
		
			path('',views.register,name='register'),
			path('',views.profile,name= 'profile'),
			]