from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('Dashboard_agent/', views.Dashboard_agent, name='Dashboard_agent'),
    path('Learning/', views.Learning, name='Learning'),

]