from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': 'Please enter correct email and password'
    }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                self.add_error(None, self.error_messages['invalid_login'])

        return cleaned_data

