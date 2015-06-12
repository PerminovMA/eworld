from django.contrib import admin
from models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name']


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Custom info'), {'fields': ('is_banned', 'phone_number', 'cities')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'is_event_manager', 'is_client', 'is_staff')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'theme', 'creation_datetime')


@admin.register(EventManager)
class EventManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'legal_status', 'activity_index')

admin.site.register(Country)
admin.site.register(Client)

admin.site.unregister(Group)