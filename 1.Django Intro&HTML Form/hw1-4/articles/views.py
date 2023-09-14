from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'menus' : ['a','b','c','d'],
        'users' : [],
    }
    return render(request, 'articles/index.html', context)