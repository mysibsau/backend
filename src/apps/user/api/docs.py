from drf_yasg import openapi


swagger_auth = {
    'operation_id': 'Auth',
    'methods': ['POST'],
    'responses': {
        200: openapi.Response(
            description='Авторизация прошла успешно',
            examples={
                'application/json': {
                    'token': 'yhtgrfe',
                    'FIO': 'Иванов Ф. Ю.',
                    'averga': 4.73,
                    'group': 'БПИ18-01',
                    'zachotka': '1234321',
                }
            }
        ),
        400: openapi.Response(
            'Не передали json или одно из полей',
            examples={
                'application/json': {'error': 'bad request'}
            }
        ),
        418: openapi.Response(
            'Переданный username не является номером зачетки',
            examples={
                'application/json': {'error': 'username is not gradebook'}
            }
        ),
        401: openapi.Response(
            'Авторизация не пройдена',
            examples={
                'application/json': {'error': 'bad auth'}
            }
        ),
    },
    'tags': ['User']
}
