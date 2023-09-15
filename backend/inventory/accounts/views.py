from django.shortcuts import render

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        username = request