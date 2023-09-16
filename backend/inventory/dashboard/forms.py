from django import forms
from . models import Product
from .forms import ProductForm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','cateory','quantity']
        
        