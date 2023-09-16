from django.contrib import admin
from .models import Product,Order,Profile
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'CURIOUS CODERS',

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','category')
    list_filter = ['category']

admin.site.register(Product,ProductAdmin)

admin.site.register(Order)

admin.site.register(Profile)
