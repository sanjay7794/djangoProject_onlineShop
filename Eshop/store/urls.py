from django.contrib import admin
from django.urls import path
from .views import index,Login
from .import views
urlpatterns = [
    path('', index,name='homepage'),
    path('signup',views.signup),
    path('login',Login.as_view())
]
