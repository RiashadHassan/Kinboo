from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path ('accounts/register/',register, name='register'),
    path ('accounts/login/',Login.as_view(), name='login')
    
]

