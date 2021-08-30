from drf_yasg import openapi

swagger_all_events = {
    'operation_id': 'All events',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('UUID', openapi.IN_QUERY, "Уникальный индификатор", type=openapi.TYPE_STRING, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список мероприятий",
            examples={
                "application/json": [
                    {
                        "id": 2,
                        "name": "Название мероприятия",
                        "logo": {
                            "url": "Ссылка на афишу",
                            "width": 1258,
                            "height": 1600
                        },
                        "text": "Текст поста",
                        "views": 0,
                        "likes": 0,
                        "is_liked": False
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
    }
}

swagger_all_news = {
    'operation_id': 'All news',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('UUID', openapi.IN_QUERY, "Уникальный индификатор", type=openapi.TYPE_STRING, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список новостей",
            examples={
                "application/json": [
                    {
                        "id": 4,
                        "text": "Текст поста",
                        "views": 19,
                        "likes": 6,
                        "is_liked": True,
                        "images": [
                            {
                                "url": "Ссылка до изображения",
                                "width": 600,
                                "height": 900
                            },
                        ]
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
    }
}

swagger_like = {
    'operation_id': 'Like',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('UUID', openapi.IN_QUERY, "Уникальный индификатор", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('post_id', openapi.IN_PATH, "Id записи", type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Лайк поставлен/убран",
            examples={
                "application/json": {'good': 'лайк поставлен/убран'}
            }
        ),
        401: openapi.Response(
            description="не указан uuid",
            examples={
                "application/json": {'error': 'not uuid'}
            }
        ),
        404: openapi.Response(
            description="не верно указан id или дата записи кончилась",
            examples={
                "application/json": {'error': 'Запись не найдена'}
            }
        ),
    }
}

swagger_view = {
    'operation_id': 'View',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('post_id', openapi.IN_PATH, "Id записи", type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Просмотр засчитан",
            examples={
                "application/json": {'good': 'просмотр засчитан'}
            }
        ),
        404: openapi.Response(
            description="не верно указан id или дата записи кончилась",
            examples={
                "application/json": {'error': 'Запись не найдена'}
            }
        ),
    },
}
