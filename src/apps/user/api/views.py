from rest_framework.response import Response
from rest_framework.decorators import api_view
from json import loads as json_loads
from api_pallada import API
from apps.user.services import getters
from drf_yasg.utils import swagger_auto_schema
from apps.user.api import docs


@swagger_auto_schema(**docs.swagger_auth)
@api_view(['POST'])
def auth(request):
    """
        Авторизация

        Ожидает json с номером зачетки и паролем

        ```
            {
                "username": "1234321",
                "password": "w0rng классный" 
            }
        ```
    """

    if not request.body:
        return Response({'error': 'bad request'}, 400)

    data = json_loads(request.body)

    username = data.get('username')
    password = data.get('password')

    if not (username and password):
        return Response({'error': 'bad request'}, 400)

    if not username.isdigit():
        return Response({'error': 'username is not gradebook'}, 418)

    api = API('portfolio', username, password)

    if not api.uid:
        return Response({'error': 'bad auth'}, 401)

    return Response(getters.get_data(api), 200)
