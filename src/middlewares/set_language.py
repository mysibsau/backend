from django.utils import translation
from django.conf import settings


def set_language(get_response):
    def middleware(request):
        default_language = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        user_language = request.GET.get("language", default_language)
        translation.activate(user_language)
        response = get_response(request)
        return response
    return middleware
