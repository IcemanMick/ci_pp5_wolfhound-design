# Lines 3 to 11 Credit Code Institute, Boutique Ado

from django.shortcuts import render

# Create your views here.

def index(request):
    """A view to return the index page """

    return render(request, 'home/index.html')
