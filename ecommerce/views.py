from django.shortcuts import render
from .models import Products


def product_page(request):
    product = Products.object.all()
    context = {
        "Products": Products
    }

    return render(request, "ecommerce/Products.html", context)
