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

def new(request):
    return render(request, 'restaurants/new.html')

def create(request):
    name = request.GET.get('name')
    description = request.GET.get('description')
    address = request.GET.get('address')
    phone_number = request.GET.get('phone_number')
    restaurant = Restaurant(name=name, description=description, 
                            address=address, phone_number=phone_number)
    restaurant.save()
    return render(request, 'restaurants/create.html')


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


def edit(request, pk):
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
    return render(request, 'restaurants/edit.html', context)

