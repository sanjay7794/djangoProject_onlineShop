from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse

from store.models.customer import Customer
from store.models.product import Product

from  django.views import View
from store.models.orders import Orders

class OrderView(View):
    def get (self,request):
        customer=request.session.get('customer')
        orders = Orders.get_product_by_customer(customer)
        print(orders)
        return render (request,'orders.html',{'orders':orders})
        