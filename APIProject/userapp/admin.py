from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ("id",)

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.list_display = ("id",) + self.list_display