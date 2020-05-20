from django.contrib import admin

import api.models as models

admin.site.register(models.Elder)
admin.site.register(models.Group)
admin.site.register(models.Subject)
admin.site.register(models.Teacher)


@admin.register(models.Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(models.TimetableGroup)
class DayAdmin(admin.ModelAdmin):
    list_filter = ('group',)
    list_display = ('group', 'day', 'even_week')


@admin.register(models.Subgroup)
class SubgroupAdmin(admin.ModelAdmin):
    list_display = ('subject', 'get_teachers', 'cabinet', 'subgroup')

    def get_teachers(self, obj):
        return ", ".join([s.name for s in obj.teacher.all()])


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', 'get_subject')

    def get_subject(self, obj):
        return ", ".join([s.subject.title for s in obj.subgroup.all()])
