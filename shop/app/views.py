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


class SigninView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signin.html')


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')


# User Profile
class ManagemyaccountView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userprofile/managemyaccount.html')


class UserprofileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userprofile/userprofile.html')


class AddressbookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userprofile/addressbook.html')


class MycancellationsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userprofile/mycancellations.html')


class MyreturnsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userprofile/myreturns.html')


class MyordersView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userprofile/myorders.html')

