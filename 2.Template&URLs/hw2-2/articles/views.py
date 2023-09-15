from django.shortcuts import render

# Create your views here.
def catch(request):
    return render(request, 'articles/catch.html')

def introduce(request, name, age):
    # name = request.GET.get('name')
    # age = request.GET.get('age')
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'articles/introduce.html', context)
    