from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.

def home(request):
	return render(request,'product/product-home.html')
def showall(request):
	products=product.objects.all()
	
	return render(request,'product/products.html',{"products":products})