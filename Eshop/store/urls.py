from django.contrib import admin
from django.urls import path
from store.Views.home import index
from .import views
from store.Views.login import Login 
from store.Views.signup import Signup 
urlpatterns = [
    path('', index,name='homepage'),
    path('signup',Signup.as_view()),
    path('login',Login.as_view())
]
