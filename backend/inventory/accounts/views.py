from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        username = request.POST['Username'],
        password = request.POST['Password'],
        
        user = auth.authenticate(username = username , password = password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request , 'invalid credentials')
            return redirect('login')
    else:
        return render(request , 'login.html')


def register(requset):
    
    if requset.method == 'POST':
        username = requset.POST['Username'],
        password1 = requset.POST['Password1'],
        password2 = requset.POST['Password2'],
        email = requset.POST['Email'],
        
        if (password1 == password2):
            if User.objects.filter(username = username).exists():
                messages.info(request , 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request , 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password = password1 , email = email)
                user.save()
                return redirect('login')
    else:
        messages.info(request, 'register.html')
        return render('register')
    


def logout(request):
    auth.logout(request)
    return redirect('/')
        
                    