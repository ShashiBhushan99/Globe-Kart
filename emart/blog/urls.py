from .import views
from django.contrib import admin
from django.urls import path
urlpatterns=[
			path('',views.home,name='blog-home'),
			path('post',views.post,name='blog-post'),
			path('login',views.login,name='blog-login'),
			path('about',views.about,name='blog-about'),
			
			]