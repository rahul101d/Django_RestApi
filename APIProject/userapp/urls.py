from django.contrib import admin
from django.urls import path
from .views import register,index,user_viewset

urlpatterns = [
    path('', index),
    path('register/', register), 
    path('userlist/',user_viewset.as_view({"get":"list"})),
    
]
