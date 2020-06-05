from django.contrib import admin
from .models import User

class PostUser(admin.ModelAdmin):
    list_display = ['name','register_date']
    list_display_links = []
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = User


admin.site.register(User, PostUser)