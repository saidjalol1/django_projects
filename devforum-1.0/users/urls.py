from django.urls import path, re_path

from django.contrib.auth.views import ( 
    LoginView,
    LogoutView,
    )   
from . import views

app_name = 'users'
urlpatterns = [

    path('registration/',views.registration, 
         name='signup'),

    path('login/', LoginView.as_view(
        template_name = 'users/login.html'), 
        name='login'
        ),
    
    path('logout/', LogoutView.as_view(
        template_name = 'users/logout.html'),
        name='logout'),

    path('profile/<int:pk>/', views.ProfileView.as_view(), 
         name='profile'),



]
