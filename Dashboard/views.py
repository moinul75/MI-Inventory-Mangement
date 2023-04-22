from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Order
from .forms import ProductAddForm,OrderRequest
#we need to authenticate the route as well to do this use login_required decorators 
from django.contrib.auth.decorators import login_required
#get the User 
from django.contrib.auth.models import User
from .models import Order,Product
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    order = Order.objects.all()
    product = Product.objects.all()
    #counts all 
    staff_counts = User.objects.all().count()
    order_counts = order.count()
    product_counts = product.count()
    #make request forms 
    if request.method == 'POST':
        form = OrderRequest(request.POST)
        if form.is_valid():
            instanse = form.save(commit=False)
            instanse.staff = request.user
            instanse.save()  
            return redirect('dashboard-index') 
    else:
        form = OrderRequest()    
    context = {
        'order':order,
        'form':form,
        'product':product,
        'staff_counts':staff_counts,
        'order_counts':order_counts,
        'product_counts':product_counts,
        
    }
    
    return render(request,'dashboard/index.html',context)


@login_required
def staff(request):
    staff = User.objects.all()
    #count all the staff,orders and products
    staff_counts = staff.count()
    order_counts = Order.objects.all().count()
    product_counts = Product.objects.all().count()
    
    context = {
        'staff':staff,
        'staff_counts':staff_counts,
        'order_counts':order_counts,
        'product_counts':product_counts,
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detials(request,pk):
    staff_id = User.objects.get(id=pk)
    context = {
        'staff_id':staff_id,
        
    }
    return render(request,'dashboard/staff_details.html',context)

@login_required(login_url='user-login')
def product(request):
    product = Product.objects.all()
    #counts all the things 
    staff_counts = User.objects.all().count()
    product_counts = product.count()
    order_counts = Order.objects.all().count()
    #adding products 
    if request.method == 'POST':
        product_add = ProductAddForm(request.POST)
        if product_add.is_valid():
            product_add.save()
            product_name = product_add.cleaned_data.get('name')
            messages.success(request,f'{product_name} in being successfully Added...')
            
            return redirect('dashboard-product')
    else:
        product_add = ProductAddForm()
    content = {
        'product':product,
        'product_add': product_add,
        'staff_counts':staff_counts,
        'order_counts':order_counts,
        'product_counts':product_counts,
    }
    return render(request,'dashboard/product.html',content)

@login_required 
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductAddForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductAddForm(instance=product)
    context = {
        'form':form
    }
    return render(request,'dashboard/product_update.html',context)

@login_required
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')
    

@login_required
def order(request):
    order = Order.objects.all()
    #counts all the products,staffs and orders 
    staff_counts = User.objects.all().count()
    product_counts =Product.objects.all().count()
    order_counts = order.count()
    content = {
        'order':order,
        'staff_counts':staff_counts,
        'order_counts':order_counts,
        'product_counts':product_counts,
    }
    return render(request,'dashboard/order.html',content)

