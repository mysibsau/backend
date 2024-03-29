from drf_yasg import openapi


swagger_join_to_union = {
    'operation_id': 'Join to union',
    'methods': ['post'],
    'manual_parameters': [
        openapi.Parameter('fio', openapi.IN_QUERY, "ФИО студента", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('institute', openapi.IN_QUERY, "институт студента", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('group', openapi.IN_QUERY, "группа студента", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('vk', openapi.IN_QUERY, "ссылка в вк на студента", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('hobby', openapi.IN_QUERY, "увлечения студента", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('reason', openapi.IN_QUERY, "причина по которой должны взять студента студента", type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('union_id', openapi.IN_PATH, "ID объединения, в которое студент хочет вступить", type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description='Заявка отправлена',
            examples={
                "application/json": {'good': 'Ваша заявка отправлена'}
            }
        ),
        400: openapi.Response(
            description='Не все поля заполнены',
            examples={
                "application/json": {'error': 'Не все поля заполнены'}
            }
        ),
        404: openapi.Response(
            description='Нельзя вступить в данное объединение',
            examples={
                "application/json": {'error': 'Нельзя вступить в данное объединение'}
            }
        ),
    },
}

swagger_all_institutes = {
    'operation_id': 'All institutes',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('language', openapi.IN_QUERY, "Язык ответа. Может быть *ru* или *en*", type=openapi.TYPE_STRING, default='ru'),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех институтов",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "name": "Название",
                        "short_name": "Короткое название",
                        "director": {
                            "image": "Фото директора института",
                            "name": "ФИО директора",
                            "address": "Адрес кабинета директора",
                            "phone": "Телефон директора",
                            "mail": "Почта директора"
                        },
                        "departments": [
                            {
                                "name": "Название кафедры",
                                "fio": "ФИО зав. кафедры",
                                "address": "Адрес кабинета",
                                "phone": "Телефон зав. кафедры",
                                "mail": "Почта зав. кафедры"
                            },
                        ],
                        "soviet": {
                            "image": "Фото председателя совета",
                            "fio": "ФИО председателя",
                            "address": "Адрес кабинета",
                            "phone": "Телефон председателя",
                            "mail": "Почта председателя"
                        }
                    },
                ]
            }
        ),
    },
}


swagger_all_buildings = {
    'operation_id': 'All buildings',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('language', openapi.IN_QUERY, "Язык ответа. Может быть *ru* или *en*", type=openapi.TYPE_STRING, default='ru'),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех корпусов",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "coast": 1,
                        "name": "Название корпуса",
                        "address": "Адрес корпуса",
                        "link": "Ссылка на 2gis",
                        "type": "Тип строения"
                    },
                ]
            }
        ),
    }
}


swagger_all_unions = {
    'operation_id': 'All unions',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('language', openapi.IN_QUERY, "Язык ответа. Может быть *ru* или *en*", type=openapi.TYPE_STRING, default='ru'),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех объединений",
            examples={
                "application/json": [
                    {
                        "rank": 1,
                        "name": "Название",
                        "short_name": "Короткое название",
                        "logo": "путь до лого",
                        "photo": "путь до фото председателя",
                        "leader_rank": "должность председателя",
                        "fio": "ФИО председателя",
                        "address": "Адрес",
                        "phone": "Телефон",
                        "group_vk": "ссылка группы в вк",
                        "page_vk": "ссылка председателя в вк",
                        "about": "Описание"
                    },
                ]
            }
        ),
    },
}

swagger_all_sport_clubs = {
    'operation_id': 'All sport clubs',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('language', openapi.IN_QUERY, "Язык ответа. Может быть *ru* или *en*", type=openapi.TYPE_STRING, default='ru'),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех спортивных секций",
            examples={
                "application/json": [
                    {
                        "logo": "/media/campus/sports/logo/name.jpg",
                        "name": "Название кружка",
                        "fio": "ФИО тренера",
                        "phone": "телефон тренера",
                        "address": "адрес проведения тренировок",
                        "dates": "дни и время тренировок"
                    }
                ]
            }
        ),
    },
}

swagger_all_design_office = {
    'operation_id': 'All design offices',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех СКБ",
            examples={
                "application/json": [
                    {
                        "id": 0,
                        "name": "Название",
                        "address": "Место расположения СКБ",
                        "fio": "Руководитель (может отсутствовать)",
                        "email": "Почта руководителя (может отсутствовать)",
                        "about": "Описание",
                    }
                ]
            }
        ),
    },
}

swagger_all_ensembles = {
    'operation_id': 'All ensemble',
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех ансамблей",
            examples={
                "application/json": [
                    {
                        "id": 0,
                        "name": "Название",
                        "logo": "Логотип",
                        "description": "Описание",
                        "achievements": "Достижения",
                        "contacts": "Контакты",
                    }
                ]
            }
        ),
    },
}
