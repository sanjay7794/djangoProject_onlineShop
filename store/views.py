from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from .models.product import *
from .models.customer import Customer
from .models.category import Category
from  django.views import View





# def signup(request):
#     if request.method == "POST":
#         data=request.POST

#         first_name=data.get('first_name')
#         last_name=data.get('last_name')
#         phone=data.get('phone')
#         email=data.get('email')
#         password=data.get('password')
        
#         customer=Customer(first_name=first_name,
#         last_name=last_name,
#         phone=phone,
#         email=email,
#         password=password)
        
#         error_msg=validateCustomer(customer)
#         if not error_msg:
#             customer.password=make_password(customer.password)  
#             customer.register()
#             error_msg="user created successfully"
#         return render(request,'signup.html',{'res':error_msg})
#     return render(request,'signup.html')
    
    
    
 