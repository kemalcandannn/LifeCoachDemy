from django.contrib import admin
from .models import Contact

class PostContact(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = []
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = Contact


admin.site.register(Contact, PostContact)