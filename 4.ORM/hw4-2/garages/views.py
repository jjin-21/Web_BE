from django.shortcuts import render
from .models import Garage

# Create your views here.
def garage(request):
    garages = Garage.objects.all()
    context = {
        'garages' : garages,
    }
    return render(request, 'index.html', context)