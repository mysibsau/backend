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
                        "id": 2,
                        "name": "Название вакансии",
                        "info": {
                            "Тут могут быть": "различные поля",
                            "Их названия": "и количество",
                            "могут меняться": "я хз как с таким API работать",
                            "но мобильщики сказали": "что классно"
                        },
                    }
                ]
            }
        ),
    },
    'tags': ['Work']
}
