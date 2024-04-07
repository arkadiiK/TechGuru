from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('products/<int:product_id>', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout')
]
