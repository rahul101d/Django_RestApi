from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NewUserForm
from django.contrib import messages
from projectapp.models import project_model
from projectapp.serializers import project_serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
# Create your views here.

#for user registration
def register(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Sucessfully")
            return HttpResponseRedirect(request.path_info)
        messages.error(request,'something wrong')
    return render(request,'userapp/register.html')

def index(request):
    return render(request,'userapp/index.html')

class user_viewset(viewsets.ViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def list(self, request):
        project=project_model.objects.filter(users=request.user)
        serializer=project_serializer(project,many=True)
        resp=[{'id':i['id'],
               "project_name":i['project_name'],
               "created_by":i['created_by'],
               'created_at':i['created_at']} 
              for i in serializer.data]
        return Response(resp)