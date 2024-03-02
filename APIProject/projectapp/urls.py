from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import project_viewset


r=DefaultRouter() 
r.register('project_api', project_viewset, basename='project')

urlpatterns =  [
    path('list/',project_viewset.as_view({"get":"list"})),    
    path('',project_viewset.as_view({"post":"create"})),
] 