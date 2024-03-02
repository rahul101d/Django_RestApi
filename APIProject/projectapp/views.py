from .models import project_model,client_model
from .serializers import project_serializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

#project get and post operation using viewsets
class project_viewset(viewsets.ViewSet):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def list(self, request,id):
        project=project_model.objects.filter(client=id)
        serializer=project_serializer(project,many=True)        
        resp=[{'id':i['id'],
               "project_name":i['project_name'],
               "users":[{
                    "id":i.users.id,
                    "name":i.users.username
                }for i in project],
               "created_by":i['created_by'],
               'created_at':i['created_at']} 
              for i in serializer.data]
        return Response(resp)
    
    def create(self, request,id):  
        data=request.data    
        try:
            user=User.objects.filter(id=data['users']['id'],username=data['users']['name'])
            if not user:
                return Response('No User Found with given id', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('There is no such user wih given id')
        try:
            ser=client_model.objects.get(id=id)
        except:
            return Response('There is no such a client', status=status.HTTP_404_NOT_FOUND)
        project=project_model.objects.create(project_name=data["project_name"],users=User.objects.get(id=data['users']['id']),client=ser,created_by=request.user)
        return Response("Project Created Successfully")

    