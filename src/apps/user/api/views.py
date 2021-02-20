from rest_framework.response import Response
from rest_framework.decorators import api_view
from json import loads as json_loads
from api_pallada import API
from apps.user import models
from apps.user.services import getters
from drf_yasg.utils import swagger_auto_schema
from apps.user.api import docs
from apps.user.services.utils import make_token
from xmlrpc.client import ProtocolError


def basic_auth(request):
    if not request.body:
        return Response({'error': 'bad request'}, 400)

    data = json_loads(request.body)

    username = data.get('username')
    password = data.get('password')

    if not (username and password):
        return Response({'error': 'bad request'}, 400)

    if not username.isdigit():
        return Response({'error': 'username is not gradebook'}, 401)

    try:
        api = API('portfolio', username, password)
    except (ProtocolError, TimeoutError):
        return Response({'error': 'error'}, 418)

    if not api.uid:
        return Response({'error': 'bad auth'}, 401)

    token = make_token(username, api.uid)
    user = models.User.objects.filter(token=token).first()
    if user and user.banned:
        return Response({'error': 'banned'}, 403)

    return api


@swagger_auto_schema(**docs.swagger_auth)
@api_view(['POST'])
def auth(request):
    """
        Auth

        Ожидает json с номером зачетки и паролем

        ```
            {
                "username": "1234321",
                "password": "w0rng классный"
            }
        ```
    """

    auth = basic_auth(request)

    if type(auth) == Response:
        return auth

    result = getters.get_data(auth)

    if result == 'banned':
        return Response({'error': 'banned'}, 403)

    return Response(result, 200)


@swagger_auto_schema(**docs.swagger_get_marks)
@api_view(['POST'])
def get_marks(request):
    """
        Get marks

        Ожидает json с номером зачетки и паролем

        ```
            {
                "username": "1234321",
                "password": "w0rng классный"
            }
        ```
    """

    auth = basic_auth(request)

    if type(auth) == Response:
        return auth

    return Response(getters.get_marks(auth), 200)


@swagger_auto_schema(**docs.swagger_get_attestation)
@api_view(['POST'])
def get_attestation(request):
    """
        Get attestation

        Ожидает json с номером зачетки и паролем

        ```
            {
                "username": "1234321",
                "password": "w0rng классный"
            }
        ```
    """
    auth = basic_auth(request)

    if type(auth) == Response:
        return auth

    return Response(getters.get_attestation(auth), 200)
