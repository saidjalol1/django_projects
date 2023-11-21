from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.HomePage.as_view(),name='home'),
    path('student/register', views.StudentCreate.as_view(), name='student_register'),
    path('hire/teacher', views.TeacherHire.as_view(), name='teacher_hiring'),
    path('add/course', views.AddCourseView.as_view(), name='add_course'),
    path('course/<int:pk>', views.CourseDetail.as_view(), name='course_detail'),
    path('payment/course_list/', views.PaymentCourseList.as_view(), name='payment_course_list'),
    path('payment/course_list/<int:pk>/', views.payment_view, name='payment')
]