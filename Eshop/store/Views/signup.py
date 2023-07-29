from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password
# Create your views here.

from store.models.customer import Customer

from django.views import View


class Signup(View):
    def get(self, request):
        return render(request,'signup.html')

    def post(self, request):
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
        
        error_msg=self.validateCustomer(customer)
        if not error_msg:
            customer.password=make_password(customer.password)  
            customer.register()
            error_msg="user created successfully"
        return render(request,'signup.html',{'res':error_msg})
        
    

    def validateCustomer(self,customer):
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
