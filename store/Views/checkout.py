from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse

from store.models.customer import Customer
from store.models.product import Product

from  django.views import View
from store.models.orders import Orders

class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer = request.session.get('customer')
        cart=request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address,phone,customer, cart,products )
        
        for product in products:
            order = Orders(customer=Customer(id=customer),
                           product=product,
                           price=product.price, 
                           address=address,
                           phone=phone,
                           quantity=cart.get(str(product.id)))
        
            order.placeOrder();
        request.session['cart']={}
        return redirect('cart')