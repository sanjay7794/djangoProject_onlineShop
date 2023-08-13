from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

from store.models.customer import Customer

from  django.views import View


class Login(View):

    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
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
                request.session['customer']=customer.id
                #request.session['email']=customer.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')

                
                
            else:
                error_msg="email or password invalid" 

 
        else:  
            error_msg="email or password invalid"    
        return render (request,'login.html',{'res':error_msg})
        
def logout(request):
    request.session.clear()
    return redirect('homepage')    