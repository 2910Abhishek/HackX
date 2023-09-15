from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
# Register your models here.



admin.site.site_header = 'CURIOUS CODERS'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')
    
    
admin.site.register(Product , ProductAdmin)