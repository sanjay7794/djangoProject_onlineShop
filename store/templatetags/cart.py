from django import template
register = template.Library()



@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

     
@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
        return cart[str(product.id)]

@register.filter(name='price_total')
def price_total(product, cart):
    return product.price*cart_quantity(product,cart)
        
@register.filter(name='cart_total')
def cart_total(product, cart):
    sum=0
    for i in product:
        sum+= price_total(i,cart)
    return sum