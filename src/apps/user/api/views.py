from rest_framework.response import Response
from rest_framework.decorators import api_view
from json import loads as json_loads
from api_pallada import API
from apps.user.services import getters, utils
from apps.user import models
from django.utils import timezone


@api_view(['POST'])
def auth(request):

    if not request.body:
        return Response({'error': 'no data'}, 403)

    data = json_loads(request.body)

    username = data.get('username')
    password = data.get('password')

    api = API('portfolio', username, password)

    if not (api.uid and username and password):
        return Response({'error': 'bad auth'}, 401)

    gradebook = getters.get_gradebook(api)
    fio, group, average = getters.get_fio_group_and_average(api)
    token = utils.make_token(fio, gradebook, group)

    user = models.User.objects.filter(token=token).first()
    if not user:
        models.User.objects.create(
            token=token,
            group=group,
            average=average,
            last_entry=timezone.localtime(),
        )
    else:
        user.average = average
        user.last_entry = timezone.localtime()
        user.save()

    return Response({
        'token': token,
        'FIO': fio,
        'averga': average,
        'group': group,
        'zachotka': gradebook,
    })
