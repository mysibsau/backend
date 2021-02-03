from drf_yasg import openapi


swagger_all_faq = {
    'operation_id': 'All FAQ',
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
    'operation_id': 'ask a question',
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
            examples={"application/json": {'error': 'not question'}}
        ),
    },
    'tags': ['Support']
}
