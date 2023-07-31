from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
# Create your views here.
from store.models.product import *

from store.models.category import Category
from  django.views import View

class Index(View):
    def post(self, request):
        product=request.POST.get('product')  
        minus=request.POST.get('minus') 
        cart=request.session.get('cart') 
        if cart:
            quantity=cart.get(product)  
            if quantity: 
                if minus=="True":
                    cart[product]=quantity-1 
                
                        
                else:
                    cart[product]=quantity+1     
            else:
                cart[product]=1            
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart  
        print('cart  :',request.session['cart'])     
        return redirect('homepage')






    def get(self, request):
        prds = None
        categori_id =request.GET.get('category')
        if categori_id:
            prds= Product.get_products_by_category_id(categori_id)
        else:
            prds = Product.get_all_products()  
        
        cat= Category.get_cat()
        data={}
        data['products']=prds
        data['cat']=cat
        print(request.session.get('email'))
        return render(request,'index.html',data ) 
        
    
    