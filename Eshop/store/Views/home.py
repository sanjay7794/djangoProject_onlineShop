from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
# Create your views here.
from store.models.product import *

from store.models.category import Category
from  django.views import View

class Index(View):
    def post(self, request):
        product_id=request.POST.get('product')
        print(product_id)
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
        
    
    