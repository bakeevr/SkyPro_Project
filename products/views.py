from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "products/product_list.html", {"products": products})