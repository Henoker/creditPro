from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomerUserChangeForm

CustomUser = get_user_model()

# Register your models here.
class CusterUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display= [
        "email",
        "username",
        "is_superuser",
    ]

admin.site.register(CustomUser, CusterUserAdmin)