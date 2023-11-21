from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'forum'
urlpatterns = [
    path('', cache_page(60*15)(views.HomePage.as_view()), name='home'),
    path('detail/<pk>', views.ProblemDetail.as_view(),name='problem_detail'),
    path('problem_add/', views.AddProblem.as_view(), name='add'),
]
