from django.test import TestCase
from django.utils import timezone
from apps.surveys import models
from random import randint, choice
from string import ascii_letters
from apps.surveys.services import getters, check
from datetime import timedelta


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

