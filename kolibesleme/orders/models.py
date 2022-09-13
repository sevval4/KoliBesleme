from time import timezone
from django.db import models

# Create your models here.

class Product(models.Model):
    STOCK=('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK')
 
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    stock=models.CharField(choices=STOCK,max_length=200)
    
    creadet_date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

def get_image_path(self):
    return '/img/'+ self.image