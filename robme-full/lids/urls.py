from django.urls import path
from . import views


app_name = 'lids'


urlpatterns = [
    path('', views.Lid.as_view(), name='lids_render'),
]