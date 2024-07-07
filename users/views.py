from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import User
from .forms import RegisterForm
from common.mixins import TitleMixin


class RegisterView(FormView, TitleMixin):
    title = 'Registration'
    model = User
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Registration successful. You can now log in."

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)

