from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Product
# Create your views here.

def index(request):
    return render(request , 'index.html')

def staff(request):
    return render(request , 'staff.html')

def product(request):
    items = Product.objects.all()
        
    context = {
        'items': items,
    }
    return render(request , 'product.html',context) 

def order(request):
    return render(request , 'order.html')

def home(request):
    return render(request , 'home.html')

def profile(request):
    return render(request , 'profile.html')