from django.urls import path
from .views import OrdersView,OrderDetail, OrdersStatusView, StorageView


app_name = 'main'
urlpatterns = [
    path('orders/', OrdersView.as_view(), name='order_page'),
    path('orders/', OrdersStatusView.as_view(), name='orders_status'),
    path('orders/<pk>', OrderDetail.as_view(), name='order_detail'),
    path('storage/', StorageView.as_view(), name='storage'),
    
]