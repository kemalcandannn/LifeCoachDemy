from django.contrib import admin
from .models import Course

class PostCourse(admin.ModelAdmin):
    list_display = ['name','subject','state']
    list_display_links = []
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Course


admin.site.register(Course, PostCourse)