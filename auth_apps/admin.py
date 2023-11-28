from django.contrib import admin
from auth_apps import models
# Register your models here.


@admin.register(models.CustomUser)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'username',
        'date_joined',
        'is_active',
        'is_staff',
    ]
