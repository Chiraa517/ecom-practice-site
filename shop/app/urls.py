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
]
