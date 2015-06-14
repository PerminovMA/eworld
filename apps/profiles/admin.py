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
        (_('Custom info'), {'fields': ('is_banned', 'phone_number', 'cities', 'about_me', 'avatar')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'is_event_manager', 'is_client', 'is_staff')

    class UserTypeFilter(admin.SimpleListFilter):
        title = _('user type')
        parameter_name = 'user_type'

        def lookups(self, request, model_admin):
            return (
                ('client', _('Client')),
                ('event_manager', _('Event manager')),
            )

        def queryset(self, request, queryset):
            if self.value() == 'client':
                return queryset.filter(client__isnull=False)
            if self.value() == 'event_manager':
                return queryset.filter(event_manager__isnull=False)

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', UserTypeFilter)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'theme', 'creation_datetime')


@admin.register(EventManager)
class EventManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'legal_status', 'activity_index')
    search_fields = ['user__email', 'user__username']

    class PortfolioInLine(admin.TabularInline):
        model = Portfolio
        extra = 1

    inlines = (PortfolioInLine,)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_index')
    search_fields = ['user__email', 'user__username']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_manager',)

    class PortfolioImageInLine(admin.TabularInline):
        model = PortfolioImage
        extra = 1

    inlines = (PortfolioImageInLine,)


admin.site.register(Country)

admin.site.unregister(Group)