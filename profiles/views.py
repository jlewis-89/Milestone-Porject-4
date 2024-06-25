from django.shortcuts import render

# Create your views here.


def profiles(request):
    """ A view to return the profiles page """
    return render(request, 'profiles/profiles.html')


def update_profile(request):
    """ A view to return the update_profiles page """
    return render(request, 'profiles/update_profile.html')
