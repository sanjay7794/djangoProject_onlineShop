from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from .models.product import *
from .models.customer import Customer
from .models.category import Category
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
    

def signup(request):
    if request.method == "POST":
        data=request.POST

        first_name=data.get('first_name')
        last_name=data.get('last_name')
        phone=data.get('phone')
        email=data.get('email')
        password=data.get('password')
        
        customer=Customer(first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        password=password)


        isExists=customer.isExists()
        if isExists:
             result="this mail is already registerd"
        else:
            customer.password=make_password(customer.password)  
            customer.register()
            result="user created successfully"
        return render(request,'signup.html',{'res':result})
    return render(request,'signup.html')
    


