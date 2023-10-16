from django.shortcuts import render

# Create your views here.
def food(request):
    foods = ['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
    context ={
        'foods': foods,
    }
    return render(request, 'menus/food.html', context)


def receipt(request):
    foods = ['피자', '치킨', '국밥', '초밥', '민초흑당로제마라탕']
    drinks = ['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']
    message = request.GET.get('message')
    context = {
        'foods': foods,
        'drinks': drinks,
        'message': message,
    }
    return render(request, 'menus/receipt.html', context)


def drink(request):
    drinks = ['cider', 'coke', 'miranda', 'fanta', 'eye of finetree']
    context = {
        'drinks': drinks,
    }
    return render(request, 'menus/drink.html', context)