from django.shortcuts import render
import random

# Create your views here.
def cer1(request):
    name = 'Kim'
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : random.choice(age),
        'grade' : random.choice(grade),
    }
    return render(request, 'certifications/certification1.html', context)

def cer2(request):
    name = 'Lee'
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : random.choice(age),
        'grade' : random.choice(grade),
    }
    return render(request, 'certifications/certification2.html', context)

def cer3(request):
    name = 'Park'
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : random.choice(age),
        'grade' : random.choice(grade),
    }
    return render(request, 'certifications/certification3.html', context)