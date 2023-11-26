from django.urls import path
from .views import StatisticsView, OrdersView,OrderDetail, OrdersStatusView


app_name = 'main'
urlpatterns = [
    path('', StatisticsView.as_view(), name='statistics'),
    path('orders/', OrdersView.as_view(), name='order_page'),
    path('orders/', OrdersStatusView.as_view(), name='orders_status'),
    path('orders/<pk>', OrderDetail.as_view(), name='order_detail'),
    
]