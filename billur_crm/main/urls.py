from django.urls import path
from .views import StatisticsView, OrdersView,OrderDetail


app_name = 'main'
urlpatterns = [
    path('', StatisticsView.as_view(), name='statistics'),
    path('orders/', OrdersView.as_view(), name='order_page'),
    path('orders/<pk>', OrderDetail.as_view(), name='order_detail'),
]