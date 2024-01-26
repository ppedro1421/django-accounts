from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class AuthCompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


class AuthUserProfileAdmin(admin.ModelAdmin):
    list_display = ['name']


class AuthUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_active', 'get_company', 'get_profile', 'is_superuser']

    @admin.display(description='Company')
    def get_company(self, obj: AuthUser):
        return obj.company.name if obj.company else None

    @admin.display(description='Profile')
    def get_profile(self, obj: AuthUser):
        return obj.profile.name if obj.profile else None


admin.site.register(AuthCompany, AuthCompanyAdmin)
admin.site.register(AuthUserProfile, AuthUserProfileAdmin)
admin.site.register(AuthUser, AuthUserAdmin)
