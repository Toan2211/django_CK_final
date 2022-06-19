from django.contrib import admin

from .models import *

class TagTublerInline(admin.TabularInline):
    model = Tag


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]
    list_display = ['title','author','date','status']
    list_editable = ['status']
    search_fields = ['title']

admin.site.register(Topic)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)

