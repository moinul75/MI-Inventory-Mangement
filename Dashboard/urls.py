from django.urls import path 
from . import views 


urlpatterns = [
    path('dash-board/',views.index,name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff/details/<str:pk>',views.staff_detials,name='dashboard-staff-details'),
    path('product/',views.product,name='dashboard-product'),
    path('product/delete/<str:pk>/',views.delete_product,name='dashboard-product-delete'),
    path('product/update/<str:pk>/',views.update_product,name='dashboard-product-update'),
    path('order/',views.order,name='dashboard-order'),
    
]
