from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem


def product_list(request):
    products = Product.objects.all()
    return render(request, 'TechGuru/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'TechGuru/product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    return redirect('product_list')


@login_required
def view_cart(request, order_item):
    order = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order.is_ordered = True
    order.save()
    return render(request, 'TechGuru/view_cart.html', {'order': order}, {'order_items': order_item})

@login_required
def checkout(request):
    order = Order.objects.get_or_create(user=request.user, is_ordered=False)
    order.is_ordered = True
    order.save()
    return render(request, 'TechGuru/checkout.html', {'order': order})
