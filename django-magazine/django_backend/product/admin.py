from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['id', 'title']
    list_per_page = 20
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount', 'is_published')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['time_created', 'id', 'price', 'discount', 'time_updated', 'is_published']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)