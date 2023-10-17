from django.shortcuts import render, redirect
from .models import Garage
from .forms import GarageForm

# Create your views here.
def index(request):
    garages = Garage.objects.all()
    context = {
        'garages': garages
    }
    return render(request, 'garages/index.html', context)

def new(request):
    return render(request, 'garages/new.html')

def create(request):
    if request.method == 'POST':
        form = GarageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('garages:index')
    else:
        form = GarageForm()
    context = {
        'form': form,
    }
    return render(request, 'garages/create.html', context)