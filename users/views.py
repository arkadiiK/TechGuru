from django.shortcuts import render, redirect
from .models import User, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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
