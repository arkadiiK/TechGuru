from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import User
from .forms import RegisterForm, LoginForm
from django.views import View
from common.mixins import RegistrationMixin, TitleMixin, LoginMixin


class RegisterView(RegistrationMixin, FormView, TitleMixin):
    title = 'Registration'
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    success_message = "Registration successful. You can now log in."


class LoginView(LoginMixin, FormView, TitleMixin):
    title = 'Login'
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('product_list')
    success_message = "User logged in."


class LogoutView(View):
    success_url = reverse_lazy('login')
    success_message = "User logged out."
