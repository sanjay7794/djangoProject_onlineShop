from django.contrib import admin
from django.urls import path
from store.Views.home import Index
from .import views
from store.Views.login import Login ,logout
from store.Views.signup import Signup 
from store.Views.cart import Cart
from store.Views.checkout import Checkout
urlpatterns = [
    path('', Index.as_view(),name='homepage'),
    path('signup',Signup.as_view()),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('cart',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='checkout')
]
