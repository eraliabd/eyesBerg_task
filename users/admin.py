from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'affiliation', 'phone_number', 'gender', 'is_active']
    list_display_links = ['id', 'username']
    list_filter = ['gender', 'is_staff', 'is_superuser', 'is_active']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('affiliation', 'phone_number', 'gender')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('first_name', 'last_name', 'affiliation', 'phone_number', 'gender')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
