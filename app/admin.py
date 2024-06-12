from django.contrib import admin
from django.utils.html import format_html

from .models import Logo, ConferenceSection


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_logo')
    list_display_links = ('id', 'title')

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "No Image"
    display_logo.short_description = 'Logo'


@admin.register(ConferenceSection)
class ConferenceSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_logo')
    list_display_links = ('id', 'title')

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "No Image"
    display_logo.short_description = 'Logo'
