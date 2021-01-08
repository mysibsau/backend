from drf_yasg import openapi


swagger_groups_hash = {
    'operation_id': 'Hash groups',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
            examples={
                "application/json": {
                    "hash": "Какой-то уникальный хэш"
                }
            }
        ),
    },
    'tags': ['Timetable']
}

swagger_teachers_hash = {
    'operation_id': 'Hash teachers',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
            examples={
                "application/json": {
                    "hash": "Какой-то уникальный хэш"
                }
            }
        ),
    },
    'tags': ['Timetable']
}


swagger_palaces_hash = {
    'operation_id': 'Hash palaces',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
            examples={
                "application/json": {
                    "hash": "Какой-то уникальный хэш"
                }
            }
        ),
    },
    'tags': ['Timetable']
}

swagger_all_groups = {
    'operation_id': 'All groups',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
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
    'tags': ['Timetable']
}

swagger_all_teachers = {
    'operation_id': 'All teachers',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
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
    'tags': ['Timetable']
}

swagger_all_places = {
    'operation_id': 'All places',
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
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
    'tags': ['Timetable']
}

swagger_timetable = {
    'methods': ['GET'],
    'responses': {
        200: openapi.Response(
            description="все гуд",
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
    'tags': ['Timetable']
}
