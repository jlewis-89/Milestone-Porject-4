# from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

# Create your views here.


def profiles(request):
    """ A view to return the profiles page """
    return render(request, 'profiles/profiles.html')


def update_profile(request):
    """ A view to return the update_profiles page """
    return render(request, 'profiles/update_profile.html')


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


# def order_history(request, order_number):
#     order = get_object_or_404(Order, order_number=order_number)

#     messages.info(request, (
#         f'This is a past confirmation for order number {order_number}. '
#         'A confirmation email was sent on the order date.'
#     ))

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#         'from_profile': True,
#     }

#     return render(request, template, context)
