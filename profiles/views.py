# from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from checkout.models import Order
from products.models import Product
from .models import Favorite
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


@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'profiles/favorites_list.html', {'favorites': favorites})


@login_required
def add_to_favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    messages.success(request, 'Product added to favorites')
    return redirect('favorites_list')

def remove_from_favorites(request, product_id):
    favorite = get_object_or_404(Favorite, user=request.user, product_id=product_id)
    favorite.delete()
    messages.success(request, 'Product removed from favorites')
    return redirect('favorites_list')
