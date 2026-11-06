from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'course']
    fieldsets = UserAdmin.fieldsets + (
        ('School Profile', {'fields': ('role', 'course')}),
    )