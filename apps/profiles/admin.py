from django.contrib import admin
from models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name']

admin.site.register(Client)
admin.site.register(EventManager)
admin.site.register(Country)
admin.site.register(City, CityAdmin)