from django.contrib import admin

import api.models as models

admin.site.register(models.Elder)
admin.site.register(models.Group)
admin.site.register(models.Subject)
admin.site.register(models.Cabinet)
admin.site.register(models.Teacher)
admin.site.register(models.Consultation)
admin.site.register(models.Session)
admin.site.register(models.Event)


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('group', 'day')


@admin.register(models.Subgroup)
class SubgroupAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'cabinet', 'subgroup')


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', 'get_subject')

    def get_subject(self, obj):
        return ", ".join([s.subject.title for s in obj.subgroup.all()])
