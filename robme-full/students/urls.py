from django.urls import path
from . import views 

app_name = 'students'
urlpatterns = [
    path('', views.StudentsView.as_view(), name='students_page'),
    path('/<pk>', views.StudentsDetailView.as_view(), name='student_detail'),
]