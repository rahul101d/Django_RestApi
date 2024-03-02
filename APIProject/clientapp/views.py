from .models import client_model
from projectapp.models import project_model
from .serializers import client_serializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import status

# Create your views here.

#client CRUD operation using viewsets
class client_viewset(viewsets.ViewSet):
    authentication_classes=[BasicAuthentication] 
    permission_classes=[IsAuthenticated]
    def list(self, request): 
        c=client_model.objects.all()
        serializer=client_serializer(c,many=True)
        resp=[{'id':i['id'],
               "client_name":i['client_name'],
               "created_by":i['created_by'],
               'created_at':i['created_at']} 
              for i in serializer.data]
        return Response(resp)
    
    def retrieve(self, request, pk):
        try:
            client=client_model.objects.get(id=pk)
        except:
            return Response("This client does not exist...")
        project=project_model.objects.filter(client=pk)
        resp={
                "id":client.id,
                "client_name":client.client_name,
                'project':[{
                    "project_id":i.id,
                    "project_name":i.project_name,
                }for i in project],
                "created_at":client.created_at,
                "created_by":client.created_by.username,
                "update_at":client.updated_at
        }
        return Response(resp)
    
    def create(self, request):
        data=request.data
        c=client_model.objects.filter(client_name=data["client_name"])
        if not c:
            client=client_model.objects.create(client_name=data["client_name"],created_by=request.user)
        else:
            return Response("client is already exits")
        return Response("client is created")
         
    def update(self,request,pk):
        try:
            client=client_model.objects.get(id=pk)
        except:
            return Response("Not client with given id") 
        serializer=client_serializer(client,data=request.data,partial=True)
        if serializer.is_valid():
            client.updated_at=timezone.now()
            serializer.save()
            return Response('data Updated')
        return Response(serializer.errors)
        
    def destroy(self,request,pk):
        try:
            c=client_model.objects.get(id=pk)
        except:
            return Response("This client does not exist...")
        c.delete()
        return Response("Data Deleted successfully...",status=status.HTTP_204_NO_CONTENT)
    
   

        