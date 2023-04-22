"""
URL configuration for Inventorymanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as user_view 
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Dashboard.urls')),
    path('',include('User.urls')),
    path('',user_view.LoginView.as_view(template_name ='user/login.html'),name='user-login',kwargs={'redirect_authenticated_user': True}),
    path('logout/',user_view.LogoutView.as_view(template_name='user/logout.html'),name='user-logout'),
    path('password_reset/',user_view.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('password_reset_done/',user_view.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',user_view.PasswordResetConfirmView.as_view(template_name='user/password_reset_confrim.html'),name='password_reset_confirm'),
    path('password_reset_complete/',user_view.PasswordResetCompleteView.as_view(template_name='user/password_reset_confirm_complete.html'),name='password_reset_complete')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
