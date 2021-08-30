from drf_yasg import openapi


swagger_groups_hash = {
    'operation_id': 'Hash groups',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся хэш групп",
            examples={
                "application/json": {
                    "hash": "Какой-то уникальный хэш"
                }
            }
        ),
    },
}

swagger_teachers_hash = {
    'operation_id': 'Hash teachers',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся хэш преподавателей",
            examples={
                "application/json": {
                    "hash": "Какой-то уникальный хэш"
                }
            }
        ),
    },
}


swagger_palaces_hash = {
    'operation_id': 'Hash palaces',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся хэш кабиентов",
            examples={
                "application/json": {
                    "hash": "Какой-то уникальный хэш"
                }
            }
        ),
    },
}

swagger_all_groups = {
    'operation_id': 'All groups',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех групп",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "name": "Название группы"
                    }
                ]
            }
        ),
    },
}

swagger_all_teachers = {
    'operation_id': 'All teachers',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех преподавателей",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "name": "ФИО препода",
                        "id_pallada": 1
                    }
                ]
            }
        ),
    },
}

swagger_all_places = {
    'operation_id': 'All places',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="Вернулся список всех кабинетов",
            examples={
                "application/json": [
                    {
                        "id": 1,
                        "name": "Название кабинета",
                        "address": "Адрес кабинета"
                    }
                ]
            }
        ),
    },
}

swagger_timetable_group = {
    'operation_id': 'Timetable group',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('group_id', openapi.IN_PATH, "Id группы", type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулось расписание группы",
            examples={
                "application/json": {
                    "object": "Название группы",
                    "even_week": [
                        {
                            "day": 0,
                            "lessons": []
                        },
                        {
                            "day": 1,
                            "lessons": []
                        },
                        {
                            "day": 2,
                            "lessons": []
                        },
                        {
                            "day": 3,
                            "lessons": []
                        },
                        {
                            "day": 4,
                            "lessons": []
                        },
                        {
                            "day": 5,
                            "lessons": []
                        }
                    ],
                    "odd_week": [
                        {
                            "day": 0,
                            "lessons": [
                                {
                                    "time": "09:40-11:10",
                                    "subgroups": [
                                        {
                                            "num": 0,
                                            "name": "Название пары",
                                            "type": 3,
                                            "teacher": "Преподаватель",
                                            "teacher_id": 1,
                                            "group": "Название группы",
                                            "group_id": 1,
                                            "place": "Кабинет",
                                            "place_id": 1
                                        }
                                    ]
                                },
                            ]
                        },
                        {
                            "day": 1,
                            "lessons": []
                        },
                        {
                            "day": 2,
                            "lessons": []
                        },
                        {
                            "day": 3,
                            "lessons": []
                        },
                        {
                            "day": 4,
                            "lessons": []
                        },
                        {
                            "day": 5,
                            "lessons": []
                        }
                    ],
                    "meta": {
                        "groups_hash": "8f331",
                        "teachers_hash": "8ae7e",
                        "places_hash": "c0a54",
                        "current_week": 1
                    }
                }
            }
        ),
        404: openapi.Response(
            description="расписание не найдено",
            examples={
                "application/json": {'error': 'Расписание не доступно'}
            }
        ),
    },
}


swagger_timetable_teacher = {
    'operation_id': 'Timetable teacher',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('teacher_id', openapi.IN_PATH, "Id преподавателя", type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулось расписание преподавателя",
            examples={
                "application/json": {
                    "object": "ФИО препода",
                    "even_week": [
                        {
                            "day": 0,
                            "lessons": []
                        },
                        {
                            "day": 1,
                            "lessons": []
                        },
                        {
                            "day": 2,
                            "lessons": []
                        },
                        {
                            "day": 3,
                            "lessons": []
                        },
                        {
                            "day": 4,
                            "lessons": []
                        },
                        {
                            "day": 5,
                            "lessons": []
                        }
                    ],
                    "odd_week": [
                        {
                            "day": 0,
                            "lessons": [
                                {
                                    "time": "09:40-11:10",
                                    "subgroups": [
                                        {
                                            "num": 0,
                                            "name": "Название пары",
                                            "type": 3,
                                            "teacher": "Преподаватель",
                                            "teacher_id": 1,
                                            "group": "Название группы",
                                            "group_id": 1,
                                            "place": "Кабинет",
                                            "place_id": 1
                                        }
                                    ]
                                },
                            ]
                        },
                        {
                            "day": 1,
                            "lessons": []
                        },
                        {
                            "day": 2,
                            "lessons": []
                        },
                        {
                            "day": 3,
                            "lessons": []
                        },
                        {
                            "day": 4,
                            "lessons": []
                        },
                        {
                            "day": 5,
                            "lessons": []
                        }
                    ],
                    "meta": {
                        "groups_hash": "8f331",
                        "teachers_hash": "8ae7e",
                        "places_hash": "c0a54",
                        "current_week": 1
                    }
                }
            }
        ),
        404: openapi.Response(
            description="расписание не найдено",
            examples={
                "application/json": {'error': 'Расписание не доступно'}
            }
        ),
    },
}


swagger_timetable_place = {
    'operation_id': 'Timetable place',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('place_id', openapi.IN_PATH, "Id кабинета", type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернулось расписание кабинета",
            examples={
                "application/json": {
                    "object": "Название кабинета",
                    "even_week": [
                        {
                            "day": 0,
                            "lessons": []
                        },
                        {
                            "day": 1,
                            "lessons": []
                        },
                        {
                            "day": 2,
                            "lessons": []
                        },
                        {
                            "day": 3,
                            "lessons": []
                        },
                        {
                            "day": 4,
                            "lessons": []
                        },
                        {
                            "day": 5,
                            "lessons": []
                        }
                    ],
                    "odd_week": [
                        {
                            "day": 0,
                            "lessons": [
                                {
                                    "time": "09:40-11:10",
                                    "subgroups": [
                                        {
                                            "num": 0,
                                            "name": "Название пары",
                                            "type": 3,
                                            "teacher": "Преподаватель",
                                            "teacher_id": 1,
                                            "group": "Название группы",
                                            "group_id": 1,
                                            "place": "Кабинет",
                                            "place_id": 1
                                        }
                                    ]
                                },
                            ]
                        },
                        {
                            "day": 1,
                            "lessons": []
                        },
                        {
                            "day": 2,
                            "lessons": []
                        },
                        {
                            "day": 3,
                            "lessons": []
                        },
                        {
                            "day": 4,
                            "lessons": []
                        },
                        {
                            "day": 5,
                            "lessons": []
                        }
                    ],
                    "meta": {
                        "groups_hash": "8f331",
                        "teachers_hash": "8ae7e",
                        "places_hash": "c0a54",
                        "current_week": 1
                    }
                }
            }
        ),
        404: openapi.Response(
            description="расписание не найдено",
            examples={
                "application/json": {'error': 'Расписание не доступно'}
            }
        ),
    },
}
