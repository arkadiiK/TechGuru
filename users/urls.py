from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(next_page='product_list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='product_list'), name='logout'),
]
