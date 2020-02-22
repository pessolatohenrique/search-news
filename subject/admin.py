from django.contrib import admin
from .models import Subject

# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    ordering = ('name', )
    fields = ('name', 'users')
    list_display = ('name', 'countUsers', )
    list_filter = ('name', 'users', )
    list_per_page = 25

    def countUsers(self, obj):
        total_users = len(obj.users.all())
        return total_users

    countUsers.short_description = 'Total Users'


admin.site.register(Subject, SubjectAdmin)
