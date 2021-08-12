from drf_yasg import openapi


swagger_all_user_faq = {
    'operation_id': 'Все FAQ авторизованного студента',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех FAQ",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "question": "Вопрос",
                        "answer": "Ответ",
                        "views": 0
                    }
                ]
            }
        ),
    },
    'tags': ['Support']
}


swagger_all_faq = {
    'operation_id': 'Всё FAQ, на которые есть ответы',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех FAQ",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "question": "Вопрос",
                        "answer": "Ответ",
                        "views": 0
                    }
                ]
            }
        ),
    },
    'tags': ['Support']
}


swagger_create_ask = {
    'operation_id': "Создание вопроса",
    'methods': ['POST'],
    'responses': {
        200: openapi.Response(
            description="Добавил вопрос",
            examples={"application/json": {'good': 'Вопрос добавлен'}}
        ),
        400: openapi.Response(
            description="Не передан JSON",
            examples={"application/json": {'error': 'JSON с ответами пуст'}}
        ),
        401: openapi.Response(
            description="Не передан вопрос",
            examples={"application/json": {'error': 'нет вопроса'}}
        ),
    },
    'tags': ['Support']
}


swagger_view_faq = {
    'operation_id': 'Просмотры FAQ',
    'methods': ['POST'],
    'manual_parameters': [
        openapi.Parameter('faq_id', openapi.IN_PATH, "Id FAQ", type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('language', openapi.IN_QUERY, "Язык ответа. Может быть *ru* или *en*", type=openapi.TYPE_STRING, default='ru'),
    ],
    'responses': {
        200: openapi.Response(
            description="Просмотр засчитан",
            examples={"application/json": {'good': 'просмотр засчитан'}}
        ),
        404: openapi.Response(
            description="Объект не найден",
            examples={"application/json": {'error': 'Запись не найдена'}}
        ),
    },
    'tags': ['Support']
}
