from django.contrib import admin
from django.urls import path
from store.Views.home import Index
from .import views
from store.Views.login import Login ,logout
from store.Views.signup import Signup 
urlpatterns = [
    path('', Index.as_view(),name='homepage'),
    path('signup',Signup.as_view()),
    path('login',Login.as_view(),name='login'),
    path('logout',logout,name='logout')
]
