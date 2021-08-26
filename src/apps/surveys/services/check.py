from apps.surveys import models
from rest_framework.response import Response
from typing import Optional


def user_already_answered(uuid: str, survey_id: int) -> bool:
    """Проверяет, ответил ли пользователь на данный опрос"""
    answers = models.Answer.objects.filter(
        who=uuid,
        survey__id=survey_id,
    ).exclude(survey__reanswer=True)
    return bool(answers.count())


def check_type_question(question_json: dict) -> bool:
    """Проверяет, совпадает ли формат ответа с типом вопроса"""
    question = models.Question.objects.filter(id=question_json['id']).first()

    # Если вопрос имеет варианты ответа
    # Но присланный json не содержит нужного поля
    if question.type in [0, 1] and 'answers' not in question_json:
        return False
    # Если вопрос имеет 1 вариант ответа
    # И длина поля != 1
    elif question.type == 0 and len(question_json['answers']) != 1:
        return False
    # Если вопрос имеет текстовый ответ
    # И не содержит текста
    elif question.type == 2 and 'text' not in question_json:
        return False
    return True


def check_contain_answer_in_question(question_json: dict) -> bool:
    """Проверяет, содержит ли вопрос данный вариант ответа"""
    question = models.Question.objects.filter(id=question_json['id']).first()
    if question.type == 2:
        return True
    answers = models.ResponseOption.objects.filter(
        id__in=question_json.get('answers'),
    )
    if not answers.count():
        return False
    for answer in answers:
        if answer.question != question:
            return False
    return True


def check_contain_answer_necessarily_question(survey_id: int, questions: list) -> bool:
    """Проверяет, заполнены ли все обязательные вопросы"""
    questions_all = models.Question.objects.filter(survey__id=survey_id)
    necessarily_question = set(
        [question.id for question in questions_all if question.necessarily],
    )
    questions_ids = set(question['id'] for question in questions)
    # Является ли множество обязательных ответов подмножеством данных ответов
    return necessarily_question <= questions_ids


def check_all(survey_id: int, questions: list) -> Optional[Response]:
    if not check_contain_answer_necessarily_question(survey_id, questions):
        return Response('Не все обязательные ответы заполнены', 405)
    for question in questions:
        if not check_type_question(question):
            return Response('Неправильная форма ответов', 405)
        elif not check_contain_answer_in_question(question):
            return Response('Вопрос не содержит такого ответа', 405)
