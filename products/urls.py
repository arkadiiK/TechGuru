from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:product_id>', views.delete_product, name='delete_product'),
]
