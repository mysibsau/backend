from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Building)
class BuildingTranslationOptions(TranslationOptions):
    fields = ('address', 'type')


@register(models.Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('name', 'address')


@register(models.Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'fio', 'address')


@register(models.Soviet)
class SovietTranslationOptions(TranslationOptions):
    fields = ('fio', 'address')


@register(models.Institute)
class InstituteTranslationOptions(TranslationOptions):
    fields = ('name', 'short_name')


@register(models.Union)
class UnionTranslationOptions(TranslationOptions):
    fields = ('name', 'short_name', 'fio', 'leader_rank', 'address', 'about')


@register(models.SportClub)
class SportClubTranslationOptions(TranslationOptions):
    fields = ('name', 'fio', 'address', 'dates')
