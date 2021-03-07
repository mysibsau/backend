from django.contrib import admin
from apps.user import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('token', 'group', 'average', 'last_entry', 'banned')
    readonly_fields = ('group', 'average', 'creation_date', 'last_entry')
