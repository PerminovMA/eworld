from django.contrib import admin
from models import Attach


class AttachAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'content_object']

admin.site.register(Attach, AttachAdmin)
