from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
# Create your views here.
from store.models.product import *

from store.models.category import Category
from  django.views import View
def index(request) :
    prds = None
    #return render(request,'orders/order.html')
    
    categori_id =request.GET.get('category')
    if categori_id:
        prds= Product.get_products_by_category_id(categori_id)
    else:
        prds = Product.get_all_products()  
    
    cat= Category.get_cat()
    data={}
    data['products']=prds
    data['cat']=cat

    return render(request,'index.html',data ) 
    