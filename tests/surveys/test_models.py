from django.test import TestCase
from apps.surveys import models
from django.utils import timezone


class SurveyModelTest(TestCase):
    def setUp(self):
        models.Survey.objects.create(
            name='Name',
            date_to = timezone.now()
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
