from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group

#change the site of Django 
admin.site.site_header = "Inventory Management"
admin.site.index_title = "Inventory Management"

#change the user model 
class ProductModel(admin.ModelAdmin):
    list_display =('name','category','quantity')
    list_filter = ['category']
# Register your models here.
admin.site.register(Product,ProductModel)
admin.site.register(Order)
admin.site.unregister(Group)


