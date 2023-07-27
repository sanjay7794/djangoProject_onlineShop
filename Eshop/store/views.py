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
    

def validateCustomer(customer):
    error_msg=None
    if(not customer.first_name):
        error_msg="first name is requred"

    elif(not customer.last_name):
        error_msg="lasst name is requred"

    elif(not customer.phone):
        error_msg="phone number is requred"

    elif(not customer.email):
        error_msg="email is requred"

    elif(not customer.password):
        error_msg="password  is requred"
    elif customer.isExists():
        error_msg="user already registerd"
    return error_msg




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
        
        error_msg=validateCustomer(customer)
        if not error_msg:
            customer.password=make_password(customer.password)  
            customer.register()
            error_msg="user created successfully"
        return render(request,'signup.html',{'res':error_msg})
    return render(request,'signup.html')
    

def login(request):
    if request.method=='POST':
        customer=Customer.objects.all()
        data=request.POST
        email=data.get('email')
        password=data.get('password')
        customer=Customer.get_customer_by_email(email)
        print(customer)
        return render (request,'login.html')

    return render (request,'login.html')
