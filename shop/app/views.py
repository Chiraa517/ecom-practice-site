from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ProductsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products.html')


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'category.html')


class CartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'checkout.html')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'about.html')


class BuynowView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'buynow.html')

