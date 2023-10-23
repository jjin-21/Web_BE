from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        next = request.POST.get('next','/')
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(next)
    else:
        form = AuthenticationForm()
        next = request.GET.get('next','/')
    context = {
        'form': form,
        'next': next,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('movies:index')