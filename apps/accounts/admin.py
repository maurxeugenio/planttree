from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Accounts


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Accounts)
