from django.shortcuts import render, redirect
from .models import Restaurant

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
    name = request.GET.get('name', 'Default Name')  # Default value
    description = request.GET.get('description', 'Default Description')
    address = request.GET.get('address', 'Default Address')
    phone_number = request.GET.get('phone_number', 'Default Phone Number')
    restaurant = Restaurant(name=name, description=description, 
                            address=address, phone_number=phone_number)
    restaurant.save()
    return render(request, 'restaurants/detail.html')
