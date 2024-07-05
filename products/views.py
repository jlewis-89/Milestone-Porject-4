from django.shortcuts import render
from . models import Product

# Create your views here.


def products(request):
    """ A view to return the products page """
    return render(request, 'products/products.html')


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product/products.html', context)
