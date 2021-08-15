from modeltranslation.translator import register, TranslationOptions
from apps.support import models


@register(models.FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(models.Theme)
class ThemeTranslationOptions(TranslationOptions):
    fields = ('title', )
