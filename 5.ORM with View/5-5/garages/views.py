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


def update(request, pk):
    garage = Garage.objects.get(pk=pk)
    if request.method == 'POST':
        form = GarageForm(request.POST, instance=garage)
        if form.is_valid():
            garage = form.save()
            return redirect('garages:index', garage.pk)
    else:
        form = GarageForm(instance=garage)
    context = {
        'garage': garage,
        'form': form,
    }
    return render(request, 'garages/update.html', context)


def delete(request, pk):
    garage = Garage.objects.get(pk=pk)
    garage.delete()
    return redirect('garages:index')