from django.contrib import admin
from .models import *

# Классы-редакторы

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'status', 'date_end', 'ls',)
    list_display_links = ('title', 'description',)
    search_fields = ('title', 'description',)


class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'board',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator')
    list_display_links = ('id',)
    search_fields = ('title',)


class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('cards', 'boards',)
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user',)
    search_fields = ('id', 'user')


admin.site.register(Card, CardAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Profile, ProfileAdmin)