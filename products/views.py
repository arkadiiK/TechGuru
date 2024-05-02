from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import ProductForm
from .models import Product
from common.mixins import TitleMixin, AddProductMixin, DeleteProductMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(TitleMixin, ListView):
    title = 'Products'
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class AddProductView(TitleMixin, AddProductMixin, ListView, LoginRequiredMixin):
    title = 'Add Product'
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('product_list')
    success_message = "Product Added Successfully"
    login_url = reverse_lazy('login')


class DeleteProductView(DeleteProductMixin, ListView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product Deleted Successfully"
    login_url = reverse_lazy('login')
