from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('staff.html',views.staff , name = 'staff'),
    path('product.html',views.product , name = 'product'),
    path('order.html',views.order, name = 'order'),
]
