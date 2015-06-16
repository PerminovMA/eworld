from django.contrib import admin
from models import Attach, Faq, FaqSection


@admin.register(Attach)
class AttachAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'content_object']


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']


@admin.register(FaqSection)
class FaqSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']