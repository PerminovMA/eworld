from django.contrib import admin
from models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name']


class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Custom info'), {'fields': ('is_banned', 'phone_number', 'cities')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Country)
admin.site.register(City, CityAdmin)

admin.site.unregister(Group)