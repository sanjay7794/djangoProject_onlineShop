from django.db import models
class Customer(models.Model):
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    phone=models.CharField(max_length=10,null=False)
    email=models.EmailField()
    password=models.CharField(max_length=500,null=False)
    def __str__(self):
        return "%s %s %s %s"%(self.first_name,self.last_name,self.phone,self.email)
    
    def register(self):
        self.save()


    @staticmethod 
    def get_customer_by_email(email):
        return Customer.objects.get(email=email)
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    
    