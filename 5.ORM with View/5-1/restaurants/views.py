from django.shortcuts import render
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