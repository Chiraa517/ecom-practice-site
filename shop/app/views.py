from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# import messages to show the error, success messages vice versa
from django.contrib import messages
# import regex for validation of email and password
import re
# importing models
from .models import Product, Category, Customer, Order, OrderStatus, City, Contry, Area, Cart


# Starting views.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        laptop = Product.objects.filter(category__title='Laptops')[:3]
        mobile = Product.objects.filter(category__title='Mobiles')[:3]
        girl_product = Product.objects.filter(category__title='Girls Fashion Product')[:3]
        category = Category.objects.all()
        print(girl_product)
        context = {
            'laptop': laptop,
            'mobile': mobile,
            'category': category,
            'girl_product': girl_product,
        }
        return render(request, 'index.html', context)


class AllProductsView(View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        context = {
            'category': category,
        }
        return render(request, 'allproducts.html', context)


class ProductsView(View):
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        category = Category.objects.all()
        context = {
            'product': product,
            'category': category,
        }
        return render(request, 'products.html', context)


class CategoryView(View):
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.filter(category__slug=slug)
        category = Category.objects.all()
        title = Category.objects.get(slug=slug)
        context = {
            'product': product,
            'category': category,
            'title': title,
        }
        return render(request, 'category.html', context)


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
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        category = Category.objects.all()
        context = {
            'product': product,
            'category': category
        }
        return render(request, 'buynow.html', context)


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
        messages.warning(request, "Username or Password is incorrect")
        return render(request, 'signin.html')


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('conpassword')
        # Todo Regex validation
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        pass_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

        if username == '':
            messages.warning(request, "Username is required")
            return redirect('signup')

        elif last_name == '':
            messages.warning(request, "Last name is required")
            return redirect('signup')

        elif first_name == '':
            messages.warning(request, "Firs name is required")
            return redirect('signup')

        if not (re.fullmatch(email_regex, email)):
            messages.warning(request, "Please enter a valid email")
            return redirect('signup')

        elif email == '':
            messages.warning(request, "Email is required")
            return redirect('signup')

        if not re.search(pass_regex, password):
            messages.warning(request, "Minimum eight characters, at least one letter, one number and one special "
                                      "character!")
            return redirect('signup')

        elif password == '':
            messages.warning(request, "Password is required")
            return redirect('signup')

        elif con_password == '':
            messages.warning(request, "Confirm Password is required")
            return redirect('signup')

        elif password != con_password:
            messages.warning(request, "Password must be same")
            return redirect('signup')

        create_users = User.objects.create_user(username, email, password)
        create_users.first_name = first_name
        create_users.last_name = last_name
        create_users.save()
        return render(request, 'signup.html')


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/signin')
