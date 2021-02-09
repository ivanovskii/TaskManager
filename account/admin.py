from django.contrib import admin
from .models import *


class CardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'list',)
    list_display_links = ('title', 'content',)
    search_fields = ('title', 'content',)


class ListsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'profile',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id',)
    search_fields = ('id',)


admin.site.register(Cards, CardsAdmin)
admin.site.register(Lists, ListsAdmin)
admin.site.register(Profile, ProfileAdmin)