from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('buynow/', views.BuynowView.as_view(), name='buynow'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    
    # user profile
    path('managemyaccount/', views.ManagemyaccountView.as_view(), name='managemyaccount'),
    path('userprofile/', views.UserprofileView.as_view(), name='userprofile'),
    path('addressbook/', views.AddressbookView.as_view(), name='addressbook'),
    path('mycancellations/', views.MycancellationsView.as_view(), name='mycancellations'),
    path('myreturns/', views.MyreturnsView.as_view(), name='myreturns'),
    path('myorders/', views.MyordersView.as_view(), name='myorders'),
]
