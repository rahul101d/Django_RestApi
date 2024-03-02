from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import client_viewset

r=DefaultRouter() 
r.register('client_api', client_viewset, basename='client')

urlpatterns =  [
    path('',include(r.urls)),
    path('client_api/<int:id>/project/',include('projectapp.urls')), 
]