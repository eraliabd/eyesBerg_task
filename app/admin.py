from django.contrib import admin
from .models import Logo, ConferenceSection


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo')
    list_display_links = ('id', 'title')


@admin.register(ConferenceSection)
class ConferenceSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo')
    list_display_links = ('id', 'title')
