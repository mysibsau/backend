from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from api.v2.menu.serializers import menu_serializers
from apps.menu.services.getters import get_menu


@api_view(['GET'])
@cache_page(60 * 60)
def all_menu(request):
    return Response(menu_serializers(get_menu()), 200)
