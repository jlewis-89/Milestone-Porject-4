from django.shortcuts import render

# Create your views here.

def profiles(request):
    """ A view to return the profiles page """
    return render(request, 'profiles/profiles.html')
