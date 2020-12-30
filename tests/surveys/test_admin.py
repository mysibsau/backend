from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from apps.surveys import models
from apps.surveys import admin
from django.test import RequestFactory
from django.utils import timezone
from datetime import timedelta
from pprint import pprint


class MockSuperUser:
    is_superuser = True


class MockUsualUser:
    is_superuser = False


class SurveyAdminTest(TestCase):
    def setUp(self):
        date = timezone.localtime() + timedelta(1)
        models.Survey.objects.create(name='Test', date_to=date)
        models.Survey.objects.create(name='Test2', date_to=timezone.localtime())
        self.request = RequestFactory().get('/admin')
        self.admin = admin.Survey(models.Survey, AdminSite())
    
    def test_count_queryset_if_user_are_super_user(self):
        """
        Количество показываемых опросов, если пользователь - админ
        """
        self.request.user = MockSuperUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 2)

    def test_count_queryset_if_user_are_usual_user(self):
        """
        Количество показываемых опросов, если пользователь - обычный
        """
        self.request.user = MockUsualUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 1)


class QuestionAdminTest(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(name='Test2', date_to=timezone.localtime())
        models.Question.objects.create(
            survey = survey,
            text = 'text',
            type = 0,
            necessarily = True
        )
        self.request = RequestFactory().get('/admin')
        self.admin = admin.Question(models.Question, AdminSite())
    
    def test_count_queryset_if_user_are_super_user(self):
        """
        Количество показываемых опросов, если пользователь - админ
        """
        self.request.user = MockSuperUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 1)

    def test_count_queryset_if_user_are_usual_user(self):
        """
        Количество показываемых опросов, если пользователь - обычный
        """
        self.request.user = MockUsualUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 0)


class ResponseOptionTest(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(
            name = 'Test2', 
            date_to=timezone.localtime()
        )
        question = models.Question.objects.create(
            survey = survey,
            text = 'text',
            type = 0,
            necessarily = True
        )
        models.ResponseOption.objects.create(
            question = question,
            text = '1'
        )
        self.request = RequestFactory().get('/admin')
        self.admin = admin.ResponseOption(models.ResponseOption, AdminSite())
    
    def test_count_queryset_if_user_are_super_user(self):
        """
        Количество показываемых опросов, если пользователь - админ
        """
        self.request.user = MockSuperUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 1)

    def test_count_queryset_if_user_are_usual_user(self):
        """
        Количество показываемых опросов, если пользователь - обычный
        """
        self.request.user = MockUsualUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 0)


class AnswerTest(TestCase):
    def setUp(self):
        survey = models.Survey.objects.create(
            name = 'Test2', 
            date_to=timezone.localtime()
        )
        question = models.Question.objects.create(
            survey = survey,
            text = 'text',
            type = 0,
            necessarily = True
        )
        models.Answer.objects.create(
            who = '123',
            survey = survey,
            question = question,
        )
        self.request = RequestFactory().get('/admin')
        self.admin = admin.Answer(models.Answer, AdminSite())
    
    def test_count_queryset_if_user_are_super_user(self):
        """
        Количество показываемых опросов, если пользователь - админ
        """
        self.request.user = MockSuperUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 1)

    def test_count_queryset_if_user_are_usual_user(self):
        """
        Количество показываемых опросов, если пользователь - обычный
        """
        self.request.user = MockUsualUser()
        queryset = self.admin.get_queryset(self.request)
        count = queryset.count()
        self.assertEqual(count, 0)
