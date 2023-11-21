from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('economy/all/', AllFinance.as_view(), name='all_finance'),
    path('economy/salary/', Salary.as_view(), name='salary'),
    path('economy/debts/', Debts.as_view(), name='debts'),
]
