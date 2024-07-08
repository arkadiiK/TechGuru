from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from .forms import ProductForm
from .models import Product
from common.mixins import TitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(TitleMixin, ListView):
    title = 'Tech Guru'
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class AddProductView(LoginRequiredMixin, TitleMixin, FormView, ListView):
    title = 'Add Product'
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product Added Successfully"
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        return super().form_valid(form)


class DeleteProductView(LoginRequiredMixin, ListView):
    model = Product
    success_url = reverse_lazy('base')
    success_message = "Product Deleted Successfully"
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(self.model, id=product_id)

        product.delete()
        return redirect('product_list')
