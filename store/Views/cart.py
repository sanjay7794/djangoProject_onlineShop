from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

from store.models.product import Product

from  django.views import View


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        
        return render(request,'cart.html',{'products':products})


    