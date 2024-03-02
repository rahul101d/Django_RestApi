from django.contrib import admin
from .models import project_model

# Register your models here.

@admin.register(project_model)
class project_admin(admin.ModelAdmin):
    list_display=["id","project_name","client","users","created_by","created_at"]
