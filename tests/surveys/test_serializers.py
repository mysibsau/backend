from django.test import TestCase
from django.utils import timezone
from apps.surveys import models, serializers
from random import randint


class SurveysSerializersTest(TestCase):
    def setUp(self):
        self.survey_attributes = {
            'id': randint(0, 100),
            'name': 'test',
            'date_to': timezone.localtime()
        }

        self.survey = models.Survey.objects.create(**self.survey_attributes)
        self.serializer = serializers.SurveysSerializers([self.survey])

    def test_len_one_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
           Нужное количество эллементов"""
        self.assertEqual(len(self.serializer), 1)

    def test_len_many_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
        Нужное количество эллементов"""
        many = randint(2, 100)
        surveys = [self.survey] * many

        self.serializer = serializers.SurveysSerializers(surveys)

        self.assertEqual(len(self.serializer), many)

    def test_contains_expected_fields(self):
        """Проверяет, содержит ли сериализованный объект все нужные поля"""
        data = self.serializer[0]
        self.assertEqual(set(data.keys()), set(['id', 'name', 'date_to']))

    def test_id_field_content(self):
        """Проверка значения поля id"""
        data = self.serializer[0]
        self.assertEqual(data['id'], self.survey_attributes['id'])

    def test_name_field_content(self):
        """Проверка значения поля name"""
        data = self.serializer[0]
        self.assertEqual(data['name'], self.survey_attributes['name'])

    def test_dateto_field_content(self):
        """Проверка значения поля date_to"""
        data = self.serializer[0]
        self.assertEqual(data['date_to'], self.survey_attributes['date_to'])


class ResponsesSerializerTest(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='test', date_to=timezone.localtime())
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
        """Проверка значения поля id"""
        data = self.serializer[0]
        self.assertEqual(data['id'], self.response_attributes['id'])

    def test_text_field_content(self):
        """Проверка значения поля text"""
        data = self.serializer[0]
        self.assertEqual(data['text'], self.response_attributes['text'])


class QuestionsSerializersTest(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='test', date_to=timezone.localtime())

        self.question_attributes = {
            'id': randint(0, 100),
            'type': randint(0, 2),
            'survey': survey,
            'text': 'test',
            'necessarily': False
        }

        self.question = models.Question.objects.create(**self.question_attributes)
        self.serializer = serializers.QuestionsSerializers([self.question])

    def test_len_one_serializer(self):
        """Проверка, содержит ли массив сериализованных объектов
           Нужное количество эллементов"""
        self.assertEqual(len(self.serializer), 1)

    def test_len_many_serializer(self):
        """Проверка длины"""
        many = randint(2, 100)
        responses = [self.question] * many

        self.serializer = serializers.ResponsesSerializer(responses)

        self.assertEqual(len(self.serializer), many)

    def test_contains_expected_fields(self):
        """Проверка наличия всех полей"""
        data = self.serializer[0]
        self.assertEqual(
            set(data.keys()), 
            set(['id', 'name', 'necessarily', 'type', 'responses'])
        )

    def test_id_field_content(self):
        """Проверка значения поля id"""
        data = self.serializer[0]
        self.assertEqual(data['id'], self.question_attributes['id'])

    def test_name_field_content(self):
        """Проверка значения поля name"""
        data = self.serializer[0]
        self.assertEqual(data['name'], self.question_attributes['text'])

    def test_necessarily_field_content(self):
        """Проверка значения поля necessarily"""
        data = self.serializer[0]
        self.assertEqual(data['necessarily'], self.question_attributes['necessarily'])

    def test_type_field_content(self):
        """Проверка значения поля type"""
        data = self.serializer[0]
        self.assertEqual(data['type'], self.question_attributes['type'])

    def test_responses_field_content(self):
        """Проверка значения поля responses"""
        data = self.serializer[0]
        self.assertEqual(data['responses'], list())

    def test_contains_expected_response(self):
        """Проверка содержит ли сериализованный объект ответ"""
        response = models.ResponseOption.objects.create(
            question=self.question,
            text='text'
        )
        serializer = serializers.QuestionsSerializers([self.question])
        data = serializer[0]
        self.assertEqual(len(data['responses']), 1)
    
    def test_contains_expected_all_responses(self):
        """Проверка содержит ли сериализованный объект все ответы"""
        response_one = models.ResponseOption.objects.create(
            question=self.question,
            text='text'
        )
        response_two = models.ResponseOption.objects.create(
            question=self.question,
            text='text'
        )
        serializer = serializers.QuestionsSerializers([self.question])
        data = serializer[0]
        self.assertEqual(len(data['responses']), 2)

    def test_not_contains_expected_responses(self):
        """Проверка не содержит ли сериализованный объект лишних ответов"""
        response_one = models.ResponseOption.objects.create(
            question=self.question,
            text='text'
        )
        survey = models.Survey.objects.create(name='test', date_to=timezone.localtime())
        question = models.Question.objects.create(
            survey=survey, 
            text='text', 
            type=0, 
            necessarily=False
        )
        response_two = models.ResponseOption.objects.create(
            question=question,
            text='text'
        )
        serializer = serializers.QuestionsSerializers([self.question])
        data = serializer[0]
        self.assertEqual(len(data['responses']), 1)


class SurveySerializersTest(TestCase):
    def setUp(self):
        self.survey_attributes = {
            'id': randint(0, 100),
            'name': 'test',
            'date_to': timezone.localtime()
        }

        self.survey = models.Survey.objects.create(**self.survey_attributes)
        self.serializer = serializers.SurveySerializers(self.survey)

    def test_contains_expected_fields(self):
        """Проверяет, содержит ли сериализованный объект все нужные поля"""
        self.assertEqual(
            set(self.serializer.keys()), 
            set(['name', 'questions'])
        )

    def test_name_field_content(self):
        """Проверка значения поля name"""
        self.assertEqual(self.serializer['name'], self.survey_attributes['name'])

    def test_questions_field_content(self):
        """Проверка значения поля questions"""
        self.assertEqual(self.serializer['questions'], list())

    def test_contains_expected_question(self):
        """Проверка содержит ли сериализованный объект вопрос"""
        question = models.Question.objects.create(
            survey=self.survey,
            text='text',
            type=0,
            necessarily=False
        )
        serializer = serializers.SurveySerializers(self.survey)
        self.assertEqual(len(serializer['questions']), 1)

    def test_contains_expected_all_questions(self):
        """Проверка содержит ли сериализованный объект все вопросы"""
        models.Question.objects.create(
            survey=self.survey,
            text='text',
            type=0,
            necessarily=False
        )
        models.Question.objects.create(
            survey=self.survey,
            text='text',
            type=0,
            necessarily=True
        )
        serializer = serializers.SurveySerializers(self.survey)
        self.assertEqual(len(serializer['questions']), 2)

    def test_not_contains_expected_all_questions(self):
        """Проверка не содержит ли сериализованный объект все вопросы"""
        models.Question.objects.create(
            survey=self.survey,
            text='text',
            type=0,
            necessarily=False
        )
        survey = models.Survey.objects.create(name='text', date_to=timezone.localtime())
        models.Question.objects.create(
            survey=survey,
            text='text',
            type=0,
            necessarily=True
        )
        serializer = serializers.SurveySerializers(self.survey)
        self.assertEqual(len(serializer['questions']), 1)
