from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    return render(request, 'home.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})


def products(request, category=None, skinType=None):
    product = Product.objects.all()
    return render(request, 'products.html', {'product': product, 'category': category, 'skinType': skinType})
