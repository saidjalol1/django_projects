from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('', views.Teachers.as_view(),name='teachers_page'),
    path('update/<pk>/', views.Teachers.as_view(),name='teachers_update'),
    path('<pk>/', views.TeacherDetail.as_view(), name='teacher_detail'),
]