from rest_framework import serializers
from .models import client_model

#client serializer
class client_serializer(serializers.ModelSerializer):
    created_by=serializers.SerializerMethodField()
    class Meta:
        model=client_model
        fields='__all__'
    def get_created_by(self,obj):
        if obj.created_by:
            return obj.created_by.username
        
       