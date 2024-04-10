from django.contrib import admin
from .models import *

class MapAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link_map')
    list_display_links = ('id', 'title')
    ordering = ['time_created', 'id', 'time_updated', 'is_published']
    list_per_page = 20

admin.site.register(Map, MapAdmin)