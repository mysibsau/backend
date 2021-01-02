from django.test import TestCase
from django.utils import timezone
from apps.surveys import models
from apps.surveys.services import setters


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
