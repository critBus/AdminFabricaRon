from django.contrib import admin
from apps.users.models import User
from django.contrib.auth.admin import UserAdmin
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),

    )
    list_filter = ("is_active", "groups",)
    list_display = ("username", "email", "first_name", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username","email", "first_name")
admin.site.register(User,MyUserAdmin)
