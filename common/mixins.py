from django.contrib.auth import logout, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView


class TitleMixin:
    title: str | None = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data()
        context['title'] = self.title
        return context


class RegistrationMixin(SuccessMessageMixin):

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)


class LoginMixin:
    error_messages = {
        'invalid_login': 'Please enter correct email and password'
    }

    def authenticate_user(self, email, password, form_instance):
        user = authenticate(email=email, password=password)
        if not user:
            form_instance.add_error(None, self.error_messages['invalid_login'])
        return user


class LogoutMixin:
    def get(self):
        logout(self)
        return redirect('login')


class AddProductMixin(FormView):
    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        return super().form_valid(form)


class DeleteProductMixin(View):
    model = None

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(self.model, id=product_id)
        product.delete()
        return redirect('product_list')
