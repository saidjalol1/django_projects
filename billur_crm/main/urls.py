from django.urls import path
from .views import StatisticsView


app_name = 'main'
urlpatterns = [
    path('', StatisticsView.as_view(), name='statistics'),
]