from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import CreationUserForm, UserLoginForm, AdminUserForm
from .models import CustomUser


@login_required
def user_logout(request):
    logout(request)
    return redirect('main')


def register(request):
    registered = False
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            request.session['id_'] = user.id
    else:
        form = CreationUserForm()

    context = {
        'form': form,
        'registered': registered,
    }
    return render(request, 'sign-in.html', context)


def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            candidate = authenticate(email=email, password=password)
            if candidate:
                login(request, candidate)
                return redirect('main')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
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


# admin side
def check_superuser(request):
    if request.user.is_anonymous:
        return False
    return request.user.role


# user CRUD
def user_list(request):
    if not check_superuser(request):
        return redirect('main')

    users = CustomUser.get_all()
    user_groups = [['Admins', users.filter(role=True)],
                   ['Users', users.filter(role=False, is_active=True)],
                   ['Not activated', users.filter(is_active=False)]]
    context = {'user_groups': user_groups}
    return render(request, 'crud/user_list.html', context)


def user_form(request, user_uuid=0):
    if not check_superuser(request):
        return redirect('main')

    user = CustomUser.get_by_id(user_uuid)
    if request.method == 'POST':
        user = CustomUser.get_by_id(user_uuid)
        form = AdminUserForm(request.POST, instance=user)
        if form.is_valid():
            if user is None:
                new_user = form.save()
                new_user.set_password(new_user.password)
                new_user.save()
            else:
                form.save()

            return redirect('admin-user-list')
    else:
        form = AdminUserForm(instance=user)

    context = {'form': form}
    return render(request, 'crud/user_form.html', context)


def delete_user(request, user_uuid):
    CustomUser.delete_by_id(user_uuid)
    return redirect('admin-user-list')

