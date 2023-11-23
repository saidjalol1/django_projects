from django.urls import path
from .views import StatisticsView, Customers, CustomersProfile


app_name = 'main'
urlpatterns = [
    path('', StatisticsView.as_view(), name='statistics'),
    path('customers/', Customers.as_view(),name='customers' ),
    path('customers/profile/', CustomersProfile.as_view(), name='profile')
]