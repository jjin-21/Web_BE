from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    diff = num1 - num2
    mul = num1 * num2
    if num2 == 0:
        div = False
    else:
        div = num1 / num2
    context = {
        'num1': num1,
        'num2': num2,
        'diff': diff,
        'mul' : mul,
        'div' : div,
    }
    return render(request, 'calculators/result.html', context)