from django.urls import path
from . import views

app_name = 'groups'
urlpatterns = [
    path('', views.GroupView.as_view(), name='group_page'),
    path('<pk>', views.GroupDetailView.as_view(), name='group_detail'),
    # path('update_attendance/<pk>', views.update_attendance, name='update_attendance'),
]