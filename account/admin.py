from django.contrib import admin
from .models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'ls',)
    list_display_links = ('title', 'content',)
    search_fields = ('title', 'content',)


class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'profile',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id',)
    search_fields = ('id',)


admin.site.register(Card, CardAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Profile, ProfileAdmin)