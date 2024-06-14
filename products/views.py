# from django.shortcuts import render

# Create your views here.

def products(request):
    """ A view to return the products page """
    return render(request, 'products/products.html')

# def all_products(request):
#     """ A view to show all products, including sorting and search queries """

#     products = Product.objects.all()

#     context = {
#         'products': products,
#     }

#     return render(request, 'products/products.html', context)

# Compare this snippet from products/urls.py:
# """
# URL configuration for products app.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.all_products, name='products'),
# ]
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.all_products, name='products'),
# ]
# Compare this snippet from products/views.py:
# from django.shortcuts import render
# from .models import Product
#
#
# def all_products(request):
#     """ A view to show all products, including sorting and search queries """
#
#     products = Product.objects.all()
#
#     context = {
#         'products': products,
#     }
#
#     return render(request, 'products/products.html', context)
# from django.shortcuts import render
# from .models import Product


# Compare this snippet from products/models.py:
# from django.db import models
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=254)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField()
#     image_url = models.URLField(max_length=1024, null=True, blank=True)
#     image_name = models.CharField(max_length=254, null=True, blank=True)
#   image_alt = models.CharField(max_length=254, null=True, blank=True)
#     image_alt = models.CharField(max_length=254, null=True, blank=True)
#     image_alt = models.CharField(max_length=254, null=True, blank=True)
#     image_alt = models.CharField(max_length=254, null=True, blank=True)
#     image_alt = models.CharField(max_length=254, null=True, blank=True)
