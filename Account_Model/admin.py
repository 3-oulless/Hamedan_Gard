from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .models import User,Profile,OTPCode,VisitCount


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
   
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["phone","email",'first_name','last_name',"is_superuser",'is_active',"is_staff","created_date"]
    list_filter = ["is_active"]
    fieldsets = [
        ('Authentication', {"fields": ["phone",'email', "password",'first_name','last_name']}),
        ("Permissions", {"fields": ["is_superuser","is_staff","is_active"]}),
        ("Group_Permissions",{"fields":['groups','user_permissions']}),
        ("Important Date",{'fields':['last_login']})
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            'Authentication',
            {
                "classes": ["wide"],
                "fields": ["phone","email",'first_name','last_name', "password1","password2","is_superuser","is_staff","is_active"],
            },
        ),
    ]
    search_fields = ["phone"]
    ordering = ["phone"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(OTPCode)
admin.site.register(VisitCount)

admin.site.unregister(Group)