from django.test import TestCase
from apps.surveys import models
from django.utils import timezone
from pprint import pprint


class SurveyModelTest(TestCase):
    def setUp(self):
        models.Survey.objects.create(
            name='Name',
            date_to = timezone.localtime()
        )

    def test_name_label(self):
        """Проверка названия поля name"""
        survey = models.Survey.objects.first()
        field_label = survey._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название опроса')

    def test_dateto_label(self):
        """Проверка названия поля date_to"""
        survey = models.Survey.objects.first()
        field_label = survey._meta.get_field('date_to').verbose_name
        self.assertEquals(field_label,'Действует до')

    def test_name_object_is_name_field(self):
        """Проверка перевода объекта в str"""
        survey = models.Survey.objects.first()
        expected_object_name = survey.name
        self.assertEqual(str(survey), expected_object_name)

    def test_name_max_length(self):
        """Проверка максимальной длины имени"""
        survey = models.Survey.objects.first()
        max_length = survey._meta.get_field('name').max_length
        self.assertEquals(max_length, 256)
        
    def test_model_verbose_name(self):
        """Проверка названия модели в единственном числе"""
        survey = models.Survey.objects.first()
        verbose_name = survey._meta.verbose_name
        self.assertEqual(verbose_name, 'Опрос')

    def test_model_verbose_name_plural(self):
        """Проверка названия модели в множественном числе"""
        survey = models.Survey.objects.first()
        verbose_name_plural = survey._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Опросы')


class QuestionModelTest(TestCase):
    def setUp(self):
        models.Survey.objects.create(
            name = 'Name',
            date_to = timezone.localtime()
        )
        
        models.Question.objects.create(
            survey = models.Survey.objects.first(),
            text = 'Text',
            type = 0,
            necessarily = False
        )

    def test_survey_label(self):
        """Проверка названия поля survey"""
        question = models.Question.objects.first()
        field_label = question._meta.get_field('survey').verbose_name
        self.assertEqual(field_label, 'Опрос')

    def test_text_label(self):
        """Проверка названия поля text"""
        question = models.Question.objects.first()
        field_label = question._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'Текст вопроса')

    def test_type_label(self):
        """Проверка названия поля type"""
        question = models.Question.objects.first()
        field_label = question._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'Тип ответа')

    def test_necessarily_label(self):
        """Проверка названия поля necessarily"""
        question = models.Question.objects.first()
        field_label = question._meta.get_field('necessarily').verbose_name
        self.assertEqual(field_label, 'Обязательно ответить')

    def test_name_object_is_text_field(self):
        """Проверка перевода объекта в str"""
        question = models.Question.objects.first()
        expected_object_name = question.text
        self.assertEqual(str(question), expected_object_name)

    def test_text_max_length(self):
        """Проверка максимальной длины текста вопроса"""
        question = models.Question.objects.first()
        max_length = question._meta.get_field('text').max_length
        self.assertEquals(max_length, 512)

    def test_type_choices(self):
        question = models.Question.objects.first()
        choices = question._meta.get_field('type').choices
        types = ((0, 'Один ответ'), (1, 'Множество ответов'), (2, 'Свой ответ'))
        self.assertEqual(choices, types)

    def test_model_verbose_name(self):
        """Проверка названия модели в единственном числе"""
        question = models.Question.objects.first()
        verbose_name = question._meta.verbose_name
        self.assertEqual(verbose_name, 'Вопрос')

    def test_model_verbose_name_plural(self):
        """Проверка названия модели в множественном числе"""
        question = models.Question.objects.first()
        verbose_name_plural = question._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Вопросы')


class ResponseOptionModelTest(TestCase):
    def setUp(self):
        models.Survey.objects.create(
            name = 'Name',
            date_to = timezone.localtime()
        )
        
        models.Question.objects.create(
            survey = models.Survey.objects.first(),
            text = 'Text',
            type = 0,
            necessarily = False
        )

        models.ResponseOption.objects.create(
            question = models.Question.objects.first(),
            text = 'Text'
        )

    def test_question_label(self):
        """Проверка названия поля question"""
        response = models.ResponseOption.objects.first()
        field_label = response._meta.get_field('question').verbose_name
        self.assertEqual(field_label, 'Вопрос')

    def test_text_label(self):
        """Проверка названия поля text"""
        response = models.ResponseOption.objects.first()
        field_label = response._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'Ответ')

    def test_name_object_is_text_field(self):
        """Проверка перевода объекта в str"""
        response = models.ResponseOption.objects.first()
        expected_object_name = response.text
        self.assertEqual(str(response), expected_object_name)

    def test_text_max_length(self):
        """Проверка максимальной длины текста ответа"""
        response = models.ResponseOption.objects.first()
        max_length = response._meta.get_field('text').max_length
        self.assertEquals(max_length, 128)

    def test_model_verbose_name(self):
        """Проверка названия модели в единственном числе"""
        response = models.ResponseOption.objects.first()
        verbose_name = response._meta.verbose_name
        self.assertEqual(verbose_name, 'Вариант ответа')

    def test_model_verbose_name_plural(self):    
        """Проверка названия модели в множественном числе"""
        response = models.ResponseOption.objects.first()
        verbose_name_plural = response._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Варианты ответов')


class AnswerModelTest(TestCase):
    def setUp(self):
        models.Survey.objects.create(
            name = 'Name',
            date_to = timezone.localtime()
        )
        
        models.Question.objects.create(
            survey = models.Survey.objects.first(),
            text = 'Text',
            type = 0,
            necessarily = False
        )
        
        models.Answer.objects.create(
            who='Test',
            survey = models.Survey.objects.first(),
            question = models.Question.objects.first(),
            text = 'Text'
        )

    def test_who_label(self):
        """Проверка названия поля who"""
        answer = models.Answer.objects.first()
        field_label = answer._meta.get_field('who').verbose_name
        self.assertEqual(field_label, 'Кто ответил')

    def test_survey_label(self):
        """Проверка названия поля survey"""
        answer = models.Answer.objects.first()
        field_label = answer._meta.get_field('survey').verbose_name
        self.assertEqual(field_label, 'Опрос')

    def test_question_label(self):
        """Проверка названия поля question"""
        answer = models.Answer.objects.first()
        field_label = answer._meta.get_field('question').verbose_name
        self.assertEqual(field_label, 'Вопрос')

    def test_answers_label(self):
        """Проверка названия поля answers"""
        answer = models.Answer.objects.first()
        field_label = answer._meta.get_field('answers').verbose_name
        self.assertEqual(field_label, 'Ответы')

    def test_text_label(self):
        """Проверка названия поля text"""
        answer = models.Answer.objects.first()
        field_label = answer._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'Текст')

    def test_who_max_length(self):
        """Проверка максимальной длины UUID"""
        answer = models.Answer.objects.first()
        max_length = answer._meta.get_field('who').max_length
        self.assertEquals(max_length, 36)

    def test_model_verbose_name(self):
        """Проверка названия модели в единственном числе"""
        answer = models.Answer.objects.first()
        verbose_name = answer._meta.verbose_name
        self.assertEqual(verbose_name, 'Ответ')

    def test_model_verbose_name_plural(self):
        """Проверка названия модели в множественном числе"""
        answer = models.Answer.objects.first()
        verbose_name_plural = answer._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Ответы')
