from drf_yasg import openapi


swagger_all_surveys = {
    'operation_id': 'All surveys',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('UUID', openapi.IN_QUERY, "Уникальный индификатор", type=openapi.TYPE_STRING, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="все гуд",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "name": "Название",
                        "date_to": "Дата окончания"
                    }
                ]
            }
        ),
        401: openapi.Response(
            description="нет uuid",
            examples={
                "application/json": {'error': 'not uuid'}
            }
        ),
    },
    'tags': ['Surveys']
}


swagger_specific_survey = {
    'operation_id': 'Specific survey',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('UUID', openapi.IN_QUERY, "Уникальный индификатор", type=openapi.TYPE_STRING, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="все гуд",
            examples={
                "application/json": {
                    "name": "Название опроса",
                    "questions": [
                        {
                            "id": 1,
                            "name": "Вопрос",
                            "necessarily": True,
                            "type": 0,
                            "responses": [
                                {
                                    "id": 1,
                                    "text": "вариант ответа"
                                },
                            ]
                        }
                    ]
                }
            }
        ),
        401: openapi.Response(
            description="нет uuid",
            examples={
                "application/json": {'error': 'not uuid'}
            }
        ),
        403: openapi.Response(
            description="uuid уже отвечал на этот опрос",
            examples={
                "application/json": {'error': 'Вы уже прогосовали'}
            }
        ),
        404: openapi.Response(
            description="Тест не найден",
            examples={
                "application/json": {'error': 'Тест не найден'}
            }
        ),
    },
    'tags': ['Surveys']
}

swagger_set_answer = {
    'operation_id': 'Set answer',
    'methods': ['POST'],
    'manual_parameters': [
        openapi.Parameter('UUID', openapi.IN_QUERY, "Уникальный индификатор", type=openapi.TYPE_STRING, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="все гуд",
            examples={
                "application/json": {'good': 'Ваши ответы записаны'}
            }
        ),
        400: openapi.Response('Не передали json'),
        401: openapi.Response("нет uuid"),
        403: openapi.Response("uuid уже отвечал на этот опрос"),
        405: openapi.Response("Ответы не прошли проверку"),
    },
    'tags': ['Surveys']
}
