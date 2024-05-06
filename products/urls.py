from django.urls import path
from .views import ProductListView, AddProductView, DeleteProductView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add-product/', AddProductView.as_view(), name='add_product'),
    path('delete-product/<int:product_id>', DeleteProductView.as_view(), name='delete_product'),
]

