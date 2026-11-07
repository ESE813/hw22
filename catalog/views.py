from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    """Главная страница каталога"""
    products = Product.objects.all()

    return render(request, 'catalog/home.html', {'products': products})


def contacts(request):
    return render(request, "contacts.html")


def product_detail(request, pk):
    """Страница одного товара с подробной информацией."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})