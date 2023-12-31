"""
URL configuration for config project.

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
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls', namespace='forum')),
    path('users/', include('users.urls', namespace='users')),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name = 'users/reset_password.html'), 
        name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'users/password_reset_done.html'), 
        name ='password_reset_done'),
    path('reset/password/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(
         template_name = 'users/password_reset_confirm.html'),
         name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'users/password_reset_complete.html'),
        name ='password_reset_complete'),
    path("__debug__/", include("debug_toolbar.urls")),
]
