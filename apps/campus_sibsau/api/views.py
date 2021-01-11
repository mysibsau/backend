from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response


from apps.campus_sibsau import models, logger
from apps.campus_sibsau.services.join_to_union import main as join_to_union_vk
from . import docs, serializers


@swagger_auto_schema(**docs.swagger_all_unions)
@api_view(['GET'])
@cache_page(60 * 60 * 2)
def all_unions(request):
    """
    Возвращает список всех объединений.
    """
    logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех объединений")
    queryset = models.Union.objects.all()
    data = serializers.UnionSerializers(queryset)
    return Response(data)


@swagger_auto_schema(**docs.swagger_join_to_union)
@api_view(['POST'])
def join_to_union(request, union_id):
    """
    Отправляет заявку о вступлении председателю *union_id* объединения.
    """
    data = {
        'fio': request.POST.get('fio'),
        'institute': request.POST.get('institute'),
        'group': request.POST.get('group'),
        'vk': request.POST.get('vk'),
        'hobby': request.POST.get('hobby'),
        'reason': request.POST.get('reason')
    }
    if not all(data.values()):
        return Response({'error': 'Не все поля заполнены'}, 400)
    url_peer = models.Union.objects.filter(id=union_id).first().page_vk
    if not url_peer or 'id' not in url_peer:
        return Response({'error': 'Нельзя вступить в данное объединение'}, 405)
    peer_id = int(url_peer.split('id')[1])
    join_to_union_vk(data, peer_id)
    return Response({'good': 'Ваша заявка отправлена'}, 200)


@swagger_auto_schema(**docs.swagger_all_institutes)
@api_view(['GET'])
@cache_page(60 * 60 * 2)
def all_institutes(request):
    """
    All institutes
    
    Возвращает список всех институтов ВУЗа.

    Поле rank служит для изменения порядка отображения элементов.
    """
    logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех институтов")
    queryset = models.Institute.objects.all().select_related()
    return Response(serializers.InstituteSerializers(queryset))


@swagger_auto_schema(**docs.swagger_all_buildings)
@api_view(['GET'])
# @cache_page(60 * 60 * 2)
def all_buildings(request):
    """
    Возвращает список всех корпусов ВУЗа.
    """
    logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех корпусов")
    queryset = models.Building.objects.all()
    return Response(serializers.BuildingSerializers(queryset))


@swagger_auto_schema(**docs.swagger_all_sport_clubs)
@api_view(['GET'])
@cache_page(60 * 60 * 2)
def all_sport_clubs(request):
    """
    Возвращает список всех спортивных кружков
    """
    logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех кружков")
    queryset = models.SportClub.objects.all()
    return Response(serializers.SportClubSerializer(queryset))
