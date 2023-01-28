from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
import re

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


# Todo User Profile
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


# Todo Sign in System
class SignInView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signin.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        return render(request, 'signin.html')


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('conpassword')
        # Todo Regex validation
        email_regex = r'/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/'
        pass_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

        if username == '':
            messages.warning(request, "Username is required")
        elif last_name == '':
            messages.warning(request, "Last name is required")
        elif first_name == '':
            messages.warning(request, "Firs name is required")
        elif re.fullmatch(email_regex, email):
            messages.warning(request, "Please enter a valid email")
        elif email == '':
            messages.warning(request, "Email is required")
        elif re.fullmatch(pass_regex, password):
            messages.warning(request, "Minimum eight characters, at least one letter, one number and one special "
                                      "character!")
        elif password == '':
            messages.warning(request, "Password is required")
        elif con_password == '':
            messages.warning(request, "Confirm Password is required")
        elif password != con_password:
            messages.warning(request, "Password must be same")

        create_users = User.objects.create_user(username, email, password)
        create_users.first_name = first_name
        create_users.last_name = last_name
        create_users.save()
        return render(request, 'signup.html')


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/signin')
