from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register',views.register, name='user-registration'),
    path('profile/',views.profile,name='dashboard-profile'),
    path('profile/update',views.update_profile,name='user-update-profile'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
