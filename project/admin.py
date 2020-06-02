from django.contrib import admin
from .models import Project

class PostProject(admin.ModelAdmin):
    list_display = ['name', 'deadline','done']
    list_display_links = []
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Project


admin.site.register(Project, PostProject)