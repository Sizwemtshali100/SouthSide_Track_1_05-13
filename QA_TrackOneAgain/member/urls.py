from django.urls import path
from . import views

urlpatterns = [
    path('LoginUser', views.LoginUser, name='LoginUser')

]
