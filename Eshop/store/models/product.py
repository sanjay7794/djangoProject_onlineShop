from django.db import models
from .category import *
from .product import *

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    desctiption = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/products/')
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()    