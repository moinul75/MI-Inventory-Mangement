from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = [
    ('Elctronics','Electronics'),
    ('Sanitary','Sanitary'),
    ('Cloth','Cloth'),
    ('Sports','Sports'),
]
class Product(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=100,choices=CATEGORY,null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f'{self.name} - {self.quantity}'
    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff = models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity = models.PositiveSmallIntegerField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self) -> str:
        return f'{self.product} ordered By {self.staff.username}'
    