# from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from checkout.models import Order
from products.models import Product
from profiles.models import Favorite
# Create your views here.


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def favorites(request):
    """ Display the user's favorite products. """
    profile = get_object_or_404(UserProfile, user=request.user)
    favorites = profile.favorites.all()

    template = 'profiles/favorites.html'
    context = {
        'favorites': favorites,
        'on_favorites_page': True
    }

    return render(request, template, context)


def add_favorite(request, product_id):
    """ Add a product to the user's favorites. """
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if product in profile.favorites.all():
        messages.info(request, 'This product is already in your favorites')
    else:
        profile.favorites.add(product)
        messages.success(request, 'Product added to your favorites')

    return redirect(reverse('product_detail', args=[product_id]))

def remove_favorite(request, product_id):
    """ Remove a product from the user's favorites. """
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    if product in profile.favorites.all():
        profile.favorites.remove(product)
        messages.success(request, 'Product removed from your favorites')
    else:
        messages.info(request, 'This product is not in your favorites')

    return redirect(reverse('product_detail', args=[product_id]))

