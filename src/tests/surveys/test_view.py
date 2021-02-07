from rest_framework.test import APIRequestFactory
from apps.surveys import models
from apps.surveys.api import views
from django.test import TestCase
from django.utils import timezone


class SurveysViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.uuid = 'TestCase'
        models.Survey.objects.create(
            name='test',
            date_to=timezone.localtime()
        )

    def test_get_all_surveys_with_uuid(self):
        """
        Проверка получения всех опросов, если указать UUID
        """
        request = self.factory.get(
            f'/v2/surveys/all/?uuid={self.uuid}'
        )
        response = views.all_surveys(request)
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, 200)

    def test_get_all_surveys_without_uuid(self):
        """
        Проверка получения всех опросов, если не указать UUID
        """
        request = self.factory.get(
            '/v2/surveys/all/'
        )
        response = views.all_surveys(request)
        self.assertEqual(response.data, {'error': 'not uuid'})
        self.assertEqual(response.status_code, 401)

    def test_get_one_surveys_without_uuid(self):
        """
        Проверка получения одного опроса, если не указать UUID
        """
        request = self.factory.get(
            '/v2/surveys/1/'
        )
        response = views.specific_survey(request, 1)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, {'error': 'not uuid'})

    def test_get_not_exist_surveys(self):
        """
        Проверка получения одного несуществующего опроса
        """
        request = self.factory.get(
            f'/v2/surveys/2/?uuid={self.uuid}'
        )
        response = views.specific_survey(request, 2)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {'error': 'Тест не найден'})

    def test_get_if_user_already_answered(self):
        """
        Проверка получения одного опроса, если пользователь его проходил
        """
        question = models.Question.objects.create(
            survey=models.Survey.objects.first(),
            text='123',
            type=0,
            necessarily=False
        )
        models.Answer.objects.create(
            who=self.uuid,
            survey=models.Survey.objects.first(),
            question=question,
            text='text'
        )
        request = self.factory.get(
            f'/v2/surveys/1/?uuid={self.uuid}'
        )
        response = views.specific_survey(request, 1)
        self.assertEqual(response.data, {'error': 'Вы уже прогосовали'})
        self.assertEqual(response.status_code, 403)

    def test_get_if_good(self):
        """
        Проверка получения одного если все указано верно
        """
        request = self.factory.get(
            f'/v2/surveys/1/?uuid={self.uuid}'
        )
        response = views.specific_survey(request, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), dict)

    def test_put_if_answered_is_null(self):
        """
        Проверка записи ответов, если ничего не передано
        """
        request = self.factory.post(
            f'/v2/surveys/1/?uuid={self.uuid}'
        )
        response = views.set_answer(request, 1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'error': 'JSON с ответами пуст'})

    def test_put_answers_surveys_if_user_already_answered(self):
        """
        Проверка записи ответов, если пользователь уже отвечал
        """
        question = models.Question.objects.create(
            survey=models.Survey.objects.first(),
            text='123',
            type=0,
            necessarily=False
        )
        models.Answer.objects.create(
            who=self.uuid,
            survey=models.Survey.objects.first(),
            question=question,
            text='text'
        )
        json = {
            'uuid': self.uuid,
            'questions': [
            ]
        }
        request = self.factory.post(
            '/v2/surveys/1/',
            json,
            'json'
        )
        response = views.set_answer(request, 1)
        self.assertEqual(response.data, {'error': 'Вы уже прогосовали'})
        self.assertEqual(response.status_code, 403)

    def test_put_answers_surveys_if_uuid_non_exist(self):
        """
        Проверка записи ответов, если не указать UUID
        """
        json = {
            'questions': [
            ]
        }
        request = self.factory.post(
            '/v2/surveys/1/',
            json,
            'json'
        )
        response = views.set_answer(request, 1)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, {'error': 'not uuid'})

    def test_put_answers_surveys_if_questions_non_exist(self):
        """
        Проверка записи ответов, если не передать ответы
        """
        json = {
            'uuid': self.uuid
        }
        request = self.factory.post(
            '/v2/surveys/1/',
            json,
            'json'
        )
        response = views.set_answer(request, 1)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data, {'error': 'не указали ответы'})

    def test_put_answers_surveys_if_good(self):
        """
        Проверка записи ответов, если все хорошо
        """
        models.Question.objects.create(
            survey=models.Survey.objects.first(),
            text='123',
            type=0,
            necessarily=False
        )
        json = {
            'uuid': self.uuid,
            'questions': [
            ]
        }
        request = self.factory.post(
            '/v2/surveys/1/',
            json,
            'json'
        )
        response = views.set_answer(request, 1)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'good': 'Ваши ответы записаны'})
