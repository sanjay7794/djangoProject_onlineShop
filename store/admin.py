from django.contrib import admin
from .models.product import *
from .models.category import *
from .models.customer import Customer
from .models.orders import Orders

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Product,AdminProduct)
# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Orders)