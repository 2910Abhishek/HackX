from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request , 'index.html')

def staff(request):
    return render(request , 'staff.html')

def product(request):
    return render(request , 'product.html')

def order(request):
    return render(request , 'order.html')


def home(request):
    return render(request , 'home.html')