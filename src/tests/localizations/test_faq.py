from django.test import TestCase
from django.urls import reverse
from django.test import Client
from apps.support.models import FAQ


class SmokeTestTimetable(TestCase):
    def setUp(self):
        self.client = Client()
        FAQ.objects.create(
            question_ru='Вопрос',
            question_en='Question',
            answer_ru='Ответ',
            answer_en='Answer',
        )

    def test_without_lang(self):
        url = reverse('support_faq')
        response = self.client.get(url)
        result = response.json()
        assert len(result) > 0
        result = result[0]
        assert result.get('question') == 'Вопрос'
        assert result.get('answer') == 'Ответ'

    def test_with_ru_lang(self):
        url = reverse('support_faq')
        response = self.client.get(url, {'language': 'ru'})
        result = response.json()
        assert len(result) > 0
        result = result[0]
        assert result.get('question') == 'Вопрос'
        assert result.get('answer') == 'Ответ'

    def test_with_en_lang(self):
        url = reverse('support_faq')
        response = self.client.get(url, {'language': 'en'})
        result = response.json()
        assert len(result) > 0
        result = result[0]
        assert result.get('question') == 'Question'
        assert result.get('answer') == 'Answer'
