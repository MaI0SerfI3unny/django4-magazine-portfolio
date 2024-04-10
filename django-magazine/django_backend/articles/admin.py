from django.contrib import admin
from .models import *

class ArticlesAdmin(admin.ModelAdmin):
    @admin.action(description='Зробити опублікованими')
    def set_published(self,request,queryset):
        queryset.update(is_published=True)

    list_display = ('id', 'title', 'link_img', 'is_published')
    list_display_links = ( 'id', 'title' )
    prepopulated_fields = { "slug": ("title",) }
    ordering = ['time_created', 'id', 'time_updated', 'is_published']
    list_per_page = 20
    actions = ['set_published']
    search_fields = ["title"]
    list_filter = ["is_published"]

admin.site.register(Articles, ArticlesAdmin)