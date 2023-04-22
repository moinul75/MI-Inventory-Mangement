from django import forms 
from .models import Product,Order


#forms for adding products 
class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','quantity']
        

#for making a staff request 
class OrderRequest(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product','order_quantity']
    
