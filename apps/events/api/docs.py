from drf_yasg import openapi


swagger_all_events = {
    'operation_id': 'All events',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Все гуд",
            examples={
                "application/json": [
                    {
                        "name": "Название мероприятия",
                        "logo": "Афиша мероприятия",
                        "text": "Текст поста",
                        "author": "Кто заказчик",
                        "links": [
                            {
                                "name": "Название ссылки",
                                "link": "Путь ссылки"
                            }
                        ]
                    }
                ]
            }
        ),
    },
    'tags': ['Events']
}
