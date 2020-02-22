from django.contrib import admin
from .models import Site
# Register your models here.


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_editable = ('url',)
    list_filter = ('name', )
    fieldsets = (
        ('Informações gerais', {
            'fields': ('name', 'url')
        }),
        ('Marcação', {
            'classes': ('collapse',),
            'fields': ('container_class', 'title_class', 'tag_title', 'published_class'),
        }),
    )


admin.site.register(Site, SiteAdmin)
