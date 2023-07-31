from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

from store.models.customer import Customer

from  django.views import View


class Login(View):
    def get(self,request):
        return render(request,'login.html')


    def post(self,request):

        error_msg=None        
        data=request.POST
        email=data.get('email')
        password=data.get('password')
        customer=Customer.get_customer_by_email(email)
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
                return redirect('homepage')
            else:
                error_msg="email or password invalid" 

 
        else:  
            error_msg="email or password invalid"    
        return render (request,'login.html',{'res':error_msg})
        
    