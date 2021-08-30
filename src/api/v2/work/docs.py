from drf_yasg import openapi


swagger_all_vacancies = {
    'operation_id': 'All vacancies',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('language', openapi.IN_QUERY, "Язык ответа. Может быть *ru* или *en*", type=openapi.TYPE_STRING, default='ru'),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список вакансий",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "name": "Название",
                        "company": "Компания",
                        "duties": "Обязаности",
                        "requirements": "Требования",
                        "conditions": "Условия",
                        "schedule": "График работы",
                        "salary": "Заработная плата",
                        "address": "Адрес",
                        "add_info": "Дополнительная информация",
                        "contacts": "Контакты",
                        "publication_date": "Дата публикации"
                    },
                ]
            }
        ),
    },
}
