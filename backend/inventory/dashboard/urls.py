from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index , name = 'index'),
    path('', views.home , name = 'home'),
    path('staff.html',views.staff , name = 'staff'),
    path('product.html',views.product , name = 'product'),
    path('order.html',views.order, name = 'order'),
    path('profile.html' , views.profile , name = 'profile'),
]
