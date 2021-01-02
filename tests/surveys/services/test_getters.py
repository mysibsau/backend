from django.test import TestCase
from django.utils import timezone
from apps.surveys import models
from random import randint, choice
from string import ascii_letters
from apps.surveys.services import getters
from datetime import timedelta


class GettersGetAllTest(TestCase):
    def setUp(self):
        self.uuid = ''.join([
            choice(ascii_letters) for _ in range(randint(10, 100))
        ])
        date = timezone.localtime() + timedelta(1)
        models.Survey.objects.create(name='Test', date_to=date)
        models.Survey.objects.create(name='Test2', date_to=date)
        models.Survey.objects.create(name='Tes3', date_to=date, reanswer=True)

    def test_user_did_not_respond(self):
        """
        Проверка колличества опросов, если пользователь ни на что не отвечал
        """
        queryset = getters.get_all_surveys_for_uuid(self.uuid)
        count = queryset.count()
        self.assertEqual(count, 3)

    def test_count_tests_if_one_old(self):
        """
        Проверка колличества опросов, если один из них истек
        """
        date = timezone.localtime() - timedelta(1)
        models.Survey.objects.create(name='Test2', date_to=date)
        queryset = getters.get_all_surveys_for_uuid(self.uuid)
        count = queryset.count()
        self.assertEqual(count, 3)

    def test_user_did_respond(self):
        """
        Проверка колличества опросов, если пользователь отвечал
        """
        index = randint(1, 2)
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

    def test_user_did_respond_on_reanswer_test(self):
        """
        Проверка колличества опросов, если пользователь отвечал на вопрос с
        повторным ответом
        """
        survey = models.Survey.objects.get(id=3)
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
        self.assertEqual(count, 3)

