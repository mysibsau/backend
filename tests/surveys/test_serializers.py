from django.test import TestCase
from django.utils import timezone
from apps.surveys import models, serializers
from random import randint


class SurveysSerializersTest(TestCase):
    def setUp(self):
        self.survey_attributes = {
            'id': randint(0, 100),
            'name': 'test',
            'date_to': timezone.now()
        }

        self.survey = models.Survey.objects.create(**self.survey_attributes)
        self.serializer = serializers.SurveysSerializers([self.survey], '1')

    def test_len_one_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
           Нужное количество эллементов"""
        self.assertEqual(len(self.serializer), 1)

    def test_len_many_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
        Нужное количество эллементов"""
        many = randint(2, 100)
        surveys = [self.survey] * many

        self.serializer = serializers.SurveysSerializers(surveys, '1')

        self.assertEqual(len(self.serializer), many)

    def test_contains_expected_fields(self):
        """Проверяет, содержит ли сериализованный объект все нужные поля"""
        data = self.serializer[0]
        self.assertEqual(set(data.keys()), set(['id', 'name', 'date_to']))

    def test_id_field_content(self):
        """Проверяет значение поля id"""
        data = self.serializer[0]
        self.assertEqual(data['id'], self.survey_attributes['id'])

    def test_name_field_content(self):
        """Проверяет значение поля name"""
        data = self.serializer[0]
        self.assertEqual(data['name'], self.survey_attributes['name'])

    def test_dateto_field_content(self):
        """Проверяет значение поля date_to"""
        data = self.serializer[0]
        self.assertEqual(data['date_to'], self.survey_attributes['date_to'])


class ResponsesSerializerTest(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='test', date_to=timezone.now())
        question = models.Question.objects.create(
            survey=survey, 
            text='text', 
            type=0, 
            necessarily=False
        )

        self.response_attributes = {
            'id': randint(0, 100),
            'question': question,
            'text': 'test'
        }

        self.response = models.ResponseOption.objects.create(**self.response_attributes)
        self.serializer = serializers.ResponsesSerializer([self.response])

    def test_len_one_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
           Нужное количество эллементов"""
        self.assertEqual(len(self.serializer), 1)

    def test_len_many_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
        Нужное количество эллементов"""
        many = randint(2, 100)
        responses = [self.response] * many

        self.serializer = serializers.ResponsesSerializer(responses)

        self.assertEqual(len(self.serializer), many)

    def test_contains_expected_fields(self):
        """Проверяет, содержит ли сериализованный объект все нужные поля"""
        data = self.serializer[0]
        self.assertEqual(set(data.keys()), set(['id', 'text']))

    def test_id_field_content(self):
        """Проверяет значение поля id"""
        data = self.serializer[0]
        self.assertEqual(data['id'], self.response_attributes['id'])

    def test_text_field_content(self):
        """Проверяет значение поля id"""
        data = self.serializer[0]
        self.assertEqual(data['text'], self.response_attributes['text'])


