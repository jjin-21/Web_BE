from django.shortcuts import render, redirect
from .models import Travel
from .forms import TravelForm

# Create your views here.
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels': travels
    }
    return render(request, 'travels/index.html', context)


def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('travels:index')
    else:
        form = TravelForm()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)


from django.http import Http404
def detail(request, pk):
    try:
        travel = Travel.objects.get(pk=pk)
    except Travel.DoesNotExist:
        raise Http404("Travel does not exist")
        
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)


def delete(request, pk):
    travel = Travel.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')


def update(request, pk):
    travel = Travel.objects.get(pk=pk)
    if request.method == 'POST':
        form = TravelForm(request.POST, instance=travel)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = TravelForm(instance=travel)
    context = {
        'travel': travel,
        'form': form,
    }
    return render(request, 'travels/update.html', context)