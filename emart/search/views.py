from django.shortcuts import render
from product.models import product

def do_search(request):
    products = product.objects.filter(ProductName__icontains=request.GET['q'])
    return render(request, "product/products.html", {"products": products})