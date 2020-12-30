from unittest import result
from django.test import TestCase
from django.utils import timezone
from apps.surveys import models
from random import randint, choice
from string import ascii_letters
from apps.surveys.services import getters, check, setters
from datetime import timedelta
from pprint import pprint


class GettersGetAllTest(TestCase):
    def setUp(self):
        self.uuid = ''.join([
            choice(ascii_letters) for _ in range(randint(10, 100))
        ])
        date = timezone.localtime() + timedelta(1)
        models.Survey.objects.create(name='Test', date_to=date)
        models.Survey.objects.create(name='Test2', date_to=date)
        models.Survey.objects.create(name='Tes3', date_to=date)

    def test_user_did_not_respond(self):
        """
        Проверка колличества опросов, если пользователь ни на что не отвечал
        """
        queryset = getters.get_all_surveys_for_uuid(self.uuid)
        count = queryset.count()
        self.assertEqual(count, 3)

    def test_user_did_respond(self):
        """
        Проверка колличества опросов, если пользователь отвечал
        """
        index = randint(1, 3)
        survey = models.Survey.objects.get(id=index)
        question = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 0,
            necessarily = False
        )
        models.Answer.objects.create(
            who = self.uuid,
            survey = survey,
            question = question,
        )

        queryset = getters.get_all_surveys_for_uuid(self.uuid)
        count = queryset.count()
        self.assertEqual(count, 2)


class CheckAlreadyAnswerTest(TestCase):
    def setUp(self):
        self.uuid = ''.join([
            choice(ascii_letters) for _ in range(randint(10, 100))
        ])
        date = timezone.localtime() + timedelta(1)
        models.Survey.objects.create(name='Test', date_to=date)

    def test_user_already_answered_if_user_did_not_respond(self):
        """
        Проверка, если пользователь ни на что не отвечал
        """
        result = check.user_already_answered(self.uuid, 1)
        self.assertEqual(result, False)

    def test_user_already_answered_if_user_did_respond(self):
        """
        Проверка, если пользователь отвечал
        """
        survey = models.Survey.objects.first()
        question = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 0,
            necessarily = False
        )
        models.Answer.objects.create(
            who = self.uuid,
            survey = survey,
            question = question,
        )

        result = check.user_already_answered(self.uuid, 1)
        self.assertEqual(result, True)


class CheckTypeQuestion(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='1', date_to=timezone.now())
        question_one_answer = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 0,
            necessarily = True
        )
        question_many_answer = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 1,
            necessarily = True
        )
        question_answer_is_text = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 2,
            necessarily = True
        )

    def test_if_question_not_contain_answers_filed(self):
        """
        Проверяет, содержит ли присланный json поле answer
        """
        json = {'id': 1, }
        result = check.check_type_question(json)
        self.assertEqual(result, False)

    def test_if_question_contain_many_answers(self):
        """
        Проверяет, не содержит ли присланный json лишних ответов
        """
        json = {'id': 1, 'answers': [0, 1]}
        result = check.check_type_question(json)
        self.assertEqual(result, False)

    def test_if_question_not_contain_text_filed(self):
        """
        Проверяет, содержит ли присланный json поле text
        """
        json = {'id': 3, }
        result = check.check_type_question(json)
        self.assertEqual(result, False)

    def test_good_question_answer_with_one_answer(self):
        """
        Проверяет, верный формат для вопроса с 1 ответом
        """
        json = {'id': 1, 'answers': [0,]}
        result = check.check_type_question(json)
        self.assertEqual(result, True)

    def test_good_question_answer_with_many_answer(self):
        """
        Проверяет, верный формат для вопроса с несколькими ответами
        """
        json = {'id': 2, 'answers': [0, 1]}
        result = check.check_type_question(json)
        self.assertEqual(result, True)

    def test_good_question_answer_with_text_answer(self):
        """
        Проверяет, верный формат для вопроса с текстовым ответом
        """
        json = {'id': 3, 'text': '123'}
        result = check.check_type_question(json)
        self.assertEqual(result, True)


class CheckContainAnswers(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='1', date_to=timezone.now())
        question_one_answer = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 0,
            necessarily = True
        )
        question_answer_is_text = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 2,
            necessarily = True
        )
        models.ResponseOption.objects.create(
            question = question_one_answer,
            text = '1'
        )
        models.ResponseOption.objects.create(
            question = question_answer_is_text,
            text = '1'
        )

    def test_question_with_text_answer(self):
        """Проверка, если вопрос имеет ответ в виде текста"""
        json = {'id': 2, 'text': '1'}
        result = check.check_contain_answer_in_question(json)
        self.assertEqual(result, True)

    def test_if_json_contain_only_right_answers(self):
        """Проверка, если присланный json не содержит лишних ответов"""
        json = {'id': 1, 'answers': [1, ]}
        result = check.check_contain_answer_in_question(json)
        self.assertEqual(result, True)

    def test_if_json_contain_only_extra_answers(self):
        """Проверка, если присланный json содержит лишние ответы"""
        json = {'id': 1, 'answers': [1, 2]}
        result = check.check_contain_answer_in_question(json)
        self.assertEqual(result, False)


class CheckNecessarilyQuestion(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='1', date_to=timezone.now())
        question_one = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 2,
            necessarily = True
        )
        question_two = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 2,
            necessarily = False
        )

    def test_if_json_contain_necessarily_question(self):
        """Проверка, если json содержит все обязательные ответы"""
        json = [{'id': 1, 'text': '1'}, {'id': 2, 'text': 2}]
        result = check.check_contain_answer_necessarily_question(1, json)
        self.assertEqual(result, True)

    def test_if_json_not_contain_necessarily_question(self):
        """Проверка, если json не содержит все обязательные ответы"""
        json = [{'id': 2, 'text': 2}, ]
        result = check.check_contain_answer_necessarily_question(1, json)
        self.assertEqual(result, False)


class CheckAll(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='1', date_to=timezone.now())
        question_one = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 1,
            necessarily = True
        )
        question_two = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 2,
            necessarily = False
        )
        models.ResponseOption.objects.create(
            question = question_one,
            text = '1'
        )

    def test_data_response_if_not_all_required_answers_filled(self):
        """
        Проверка текста ошибки, если
        Не все обязательные ответы заполнены
        """
        json = [{'id': 2, 'text': 2}, ]
        result = check.check_all(1, json)
        self.assertEqual(result.data, 'Не все обязательные ответы заполнены')

    def test_status_code_response_if_not_all_required_answers_filled(self):
        """
        Проверка кода ошибки, если
        Не все обязательные ответы заполнены
        """
        json = [{'id': 2, 'text': 2}, ]
        result = check.check_all(1, json)
        self.assertEqual(result.status_code, 405)

    def test_data_response_if_incorrect_form_responses(self):
        """
        Проверка текста ошибки, если
        Неправильная форма ответов
        """
        json = [{'id': 1, 'text': [1, ]}, ]
        result = check.check_all(1, json)
        self.assertEqual(result.data, 'Неправильная форма ответов')

    def test_status_code_response_if_incorrect_form_responses(self):
        """
        Проверка кода ошибки, если
        Неправильная форма ответов
        """
        json = [{'id': 1, 'text': [1, ]}, ]
        result = check.check_all(1, json)
        self.assertEqual(result.status_code, 405)

    def test_data_response_if_question_not_contain_this_answer(self):
        """
        Проверка текста ошибки, если
        Вопрос не содержит такого ответа
        """
        json = [{'id': 1, 'answers': [2, ]}, ]
        result = check.check_all(1, json)
        self.assertEqual(result.data, 'Вопрос не содержит такого ответа')

    def test_status_code_response_if_incorrect_form_responses(self):
        """
        Проверка кода ошибки, если
        Вопрос не содержит такого ответа
        """
        json = [{'id': 1, 'answers': [2, ]}, ]
        result = check.check_all(1, json)
        self.assertEqual(result.status_code, 405)

    def test_if_json_right(self):
        """
        Проверка результата работы, если все хорошо
        """
        json = [{'id': 1, 'answers': [1, ]}, {'id': 2, 'text': '123'}]
        result = check.check_all(1, json)
        self.assertEqual(result, None)


class SetAnswers(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='1', date_to=timezone.now())
        question_one = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 1,
            necessarily = True
        )
        question_two = models.Question.objects.create(
            survey = survey,
            text = '1',
            type = 2,
            necessarily = False
        )
        models.ResponseOption.objects.create(
            question = question_one,
            text = '1'
        )
    
    def test_drop_error(self):
        """
        Проверка результата, если выпала ошибка
        """
        json = {
            'uuid': '123',
            'questions': [
                {'id': 1, 'answers': [2, ]}
            ]
        }
        result = setters.set_answers(json, 1)
        self.assertEqual(result.status_code, 405)

    def test_status_code_if_json_right(self):
        """
        Проверка результата, если все хорошо
        """
        json = {
            'uuid': '123',
            'questions': [
                {'id': 1, 'answers': [1, ]},
                {'id': 2, 'text': '123'}
            ]
        }
        result = setters.set_answers(json, 1)
        self.assertEqual(result.status_code, 200)

    def test_data_if_json_right(self):
        """
        Проверка результата, если все хорошо
        """
        json = {
            'uuid': '123',
            'questions': [
                {'id': 1, 'answers': [1, ]},
                {'id': 2, 'text': '123'}
            ]
        }
        result = setters.set_answers(json, 1)
        self.assertEqual(result.data, 'good')

    def test_count_recorded_answers(self):
        json = {
            'uuid': '123',
            'questions': [
                {'id': 1, 'answers': [1, ]},
                {'id': 2, 'text': '123'}
            ]
        }
        setters.set_answers(json, 1)
        count = models.Answer.objects.all().count()
        self.assertEqual(count, 2)
