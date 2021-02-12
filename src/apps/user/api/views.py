from rest_framework.response import Response
from rest_framework.decorators import api_view
from json import loads as json_loads
from api_pallada import API
from apps.user.services import getters


# portfolio_science.grade_attistation_view - аттестации
# portfolio_science.grade_view - оценки

@api_view(['POST'])
def auth(request):

    if not request.body:
        return Response({'error': 'no data'}, 403)

    data = json_loads(request.body)

    username = data.get('username')
    password = data.get('password')

    api = API('portfolio', username, password)

    if not api.uid:
        return Response({'error': 'bad auth'}, 401)

    fio, group, average = getters.get_fio_group_and_average(api)
    gradebook = getters.get_gradebook(api)

    return Response({
        'token': None,
        'FIO': fio,
        'averga': average,
        'group': group,
        'zachotka': gradebook,
    })
