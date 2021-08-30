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
        403: openapi.Response(
            'Пользователь заблокирован',
            examples={
                'application/json': {'error': 'banned'}
            }
        ),
        418: openapi.Response(
            'Палада лежит',
            examples={
                'application/json': {'error': 'error'}
            }
        ),
        401: openapi.Response(
            'Авторизация не пройдена',
            examples={
                'application/json': {'error': 'bad auth'}
            }
        ),
    },
}


swagger_get_marks = {
    'operation_id': 'get marks',
    'methods': ['POST'],
    'responses': {
        200: openapi.Response(
            description='Удалось получить оценки',
            examples={
                'application/json': [
                    {
                        'term': '1',
                        'items': [
                            {
                                'name': 'Математический анализ',
                                'mark': '4',
                                'type': 'Экзамен',
                                'coursework': None
                            }
                        ],
                    },
                    {
                        'term': '2',
                        'items': [
                            {
                                'name': 'Культурология',
                                'mark': 'Зачтено',
                                'type': 'Зачет',
                                'coursework': None
                            },
                            {
                                'name': 'БД',
                                'mark': '5/5',
                                'type': 'Зачет с оценкой',
                                'coursework': 'Какое-то название'
                            }
                        ]
                    }
                ]
            }
        ),
        400: openapi.Response(
            'Не передали json или одно из полей',
            examples={
                'application/json': {'error': 'bad request'}
            }
        ),
        403: openapi.Response(
            'Пользователь заблокирован',
            examples={
                'application/json': {'error': 'banned'}
            }
        ),
        418: openapi.Response(
            'Палада лежит',
            examples={
                'application/json': {'error': 'error'}
            }
        ),
        401: openapi.Response(
            'Авторизация не пройдена',
            examples={
                'application/json': {'error': 'bad auth'}
            }
        ),
    },
}


swagger_get_attestation = {
    'operation_id': 'get attestation',
    'methods': ['POST'],
    'responses': {
        200: openapi.Response(
            description='Удалось получить аттестацию',
            examples={
                'application/json': [
                    {
                        'name': 'Базы данных',
                        'type': 'Зачет с оценкой / КР',
                        'att1': '23',
                        'att2': '50',
                        'att3': '50',
                        'att': 'отлично'
                    },
                    {
                        'name': 'Инструментальные средства информационных систем',
                        'type': 'Экзамен',
                        'att1': '25',
                        'att2': '50',
                        'att3': '50',
                        'att': 'отлично'
                    },
                ]
            }
        ),
        400: openapi.Response(
            'Не передали json или одно из полей',
            examples={
                'application/json': {'error': 'bad request'}
            }
        ),
        403: openapi.Response(
            'Пользователь заблокирован',
            examples={
                'application/json': {'error': 'banned'}
            }
        ),
        418: openapi.Response(
            'Палада лежит',
            examples={
                'application/json': {'error': 'error'}
            }
        ),
        401: openapi.Response(
            'Авторизация не пройдена',
            examples={
                'application/json': {'error': 'bad auth'}
            }
        ),
    },
}
