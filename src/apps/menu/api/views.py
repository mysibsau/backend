from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from apps.menu.api.serializers import menu_serializers
from apps.menu.models import Menu


@api_view(['GET'])
@cache_page(60 * 60)
def all_menu(request):
    queryset = Menu.objects.all()
    return Response(menu_serializers(queryset), 200)
