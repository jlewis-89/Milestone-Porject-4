"""
URL configuration for boutique_ado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('remove_from_favorites/<int:product_id>/',
         views.remove_from_favorites, name='remove_from_favorites'),
    path('add_to_favorites/<int:product_id>/',
         views.add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.favorites_list, name='favorites_list'),
    path('password_reset/', views.password_reset, name='password_reset'),
]
