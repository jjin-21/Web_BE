from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.
def restaurants(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurants' : restaurant
    }
    return render(request, 'restaurants/restaurants.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('restaurants:detail')
    else:
        form = RestaurantForm()
    context = {
        'form': form,
    }
    return render(request, 'restaurants/create.html', context)


def delete(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    restaurant.delete()
    return redirect('restaurants:restaurants')


def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'restaurants/detail.html', context)


def update(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:restaurants', restaurant.pk)
    else:
        form = RestaurantForm(instance=restaurant)
    context = {
        'restaurant': restaurant,
        'form': form,
    }
    return render(request, 'restaurants/update.html', context)

