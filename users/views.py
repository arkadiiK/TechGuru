from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout


# home page
def index(request):
    return render(request, 'index.html')


# registration page
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            hashed_password = make_password(password)

            user = User.objects.create_user(name=name, surname=surname, email=email, password=hashed_password)

            return redirect('home')
        else:
            form = RegisterForm()

        return render(request, 'registration/register.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
