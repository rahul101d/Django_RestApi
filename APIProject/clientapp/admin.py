from django.contrib import admin
from .models import client_model
# Register your models here.

@admin.register(client_model)
class Client_admin(admin.ModelAdmin):
    list_display=["id","client_name","created_at","created_by","updated_at"]
