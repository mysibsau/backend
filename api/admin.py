from django.contrib import admin

import api.models as models

admin.site.register(models.Group)
admin.site.register(models.Subject)
admin.site.register(models.Professor)


@admin.register(models.TimetableGroup)
class TimetableGroupAdmin(admin.ModelAdmin):
    list_filter = ('group',)
    list_display = ('group', 'day', 'even_week')
    

@admin.register(models.TimetablePlace)
class TimetablePlaceAdmin(admin.ModelAdmin):
    list_filter = ('place',)
    list_display = ('place', 'day', 'even_week')


@admin.register(models.TimetableProfessor)
class TimetableProfessorAdmin(admin.ModelAdmin):
    list_filter = ('professor',)
    list_display = ('professor', 'day', 'even_week')


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Subgroup)
class SubgroupAdmin(admin.ModelAdmin):
    list_display = ('subject', 'get_professors', 'get_groups','subject', 'place', 'num')
    list_filter = ('professors', 'groups', 'place',)
    
    def get_professors(self, obj):
        return ", ".join([p.name for p in obj.professors.all()])

    def get_groups(self, obj):
        return ", ".join([p.name for p in obj.groups.all()])


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('time', 'get_subject')

    def get_subject(self, obj):
        return ", ".join([s.subject.title for s in obj.subgroup.all()])
