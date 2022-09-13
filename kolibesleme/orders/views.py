from itertools import product
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    product= Product.objects.all()
 
    context ={
        'product': product

    }
    return render(request,'orders/list.html')


def detail(request):
    return render(request,'product/detail.html')
