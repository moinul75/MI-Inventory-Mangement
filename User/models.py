from django.db import models
from django.contrib.auth.models import User 



# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='profile-image',default='avatar.jpg')
    
    def __str__(self):
        return f'{self.staff.username} -- Profiles'
    
    
    
