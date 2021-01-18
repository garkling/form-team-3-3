from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import UserForm
from .models import CustomUser


def index(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('main')


def register(request):
    registered = False
    failed = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            request.session['id_'] = user.id
        else:
            failed = True

    user_form = UserForm()
    context = {
        'form': user_form,
        'registered': registered,
        'failed': failed
    }
    return render(request, 'sign-in.html', context)


def log_in(request):
    failed = False
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        candidate = authenticate(email=email, password=password)
        if candidate:
            login(request, candidate)
            return redirect('main')
        else:
            failed = True

    user_form = UserForm()
    context = {
        'form': user_form,
        'failed': failed
    }
    return render(request, 'log-in.html', context)


def change_status(request):
    current_user = CustomUser.objects.get(id=request.session['id_'])
    if current_user:
        if current_user.is_active:
            return HttpResponse('Your account is already activated!')

        current_user.is_active = True
        current_user.save()
        return redirect('log-in')

    return HttpResponse("User is not exists!")
