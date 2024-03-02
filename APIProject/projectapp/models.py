from django.db import models
from django.contrib.auth.models import User
from clientapp.models import client_model

#project model
class project_model(models.Model):
    project_name=models.CharField(max_length=50)
    client=models.ForeignKey(client_model,on_delete=models.CASCADE)
    users=models.ForeignKey(User,on_delete=models.CASCADE,related_name='assigned_users')
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by')