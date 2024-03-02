from .models import project_model
from rest_framework import serializers

#project serializer
class project_serializer(serializers.ModelSerializer):
    client=serializers.SerializerMethodField()
    created_by=serializers.SerializerMethodField()
    users=serializers.SerializerMethodField()
    class Meta:
        model=project_model
        fields='__all__'
    def get_client(self,obj):
        if obj.client:
            return obj.client.client_name 
    def get_created_by(self,obj):
        if obj.created_by:
            return obj.created_by.username
    def get_users(self,obj):
        if obj.users:
            return obj.created_by.username