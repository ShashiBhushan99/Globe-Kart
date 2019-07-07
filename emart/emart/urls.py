"""emart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views import static
from .settings import MEDIA_ROOT
from checkout import urls as urls_checkout
from search import urls as urls_search

from user import views as user_views
from django.contrib.auth import views as auth_views


from api.resources import PostResource

from cart import urls as urls_cart
from product import urls as urls_product
from accounts import urls as urls_accounts 

post_resource= PostResource()

urlpatterns = [
    url(r'^media/(?P<path>.*)$' , static.serve,{'document_root':MEDIA_ROOT}),
    path('admin/', admin.site.urls),
	#path('', include('payments.urls')),  new
	#path('blog/',include('blog.urls')),
	path('accounts/', include('django.contrib.auth.urls')), # new
	path('register/',user_views.register,name='register'),
	path('profile/', user_views.profile, name='profile'),
	path('login/',auth_views.LoginView.as_view(template_name="user/login.html"),name="login"),
	path('logout/',auth_views.LogoutView.as_view(template_name="user/logout.html"),name="logout"),
    path('api/',include(post_resource.urls)),
	path('products/',include(urls_product)),
	url('cart/', include(urls_cart)),
	url('checkout/', include(urls_checkout)),
	url('search/', include(urls_search)),
]
