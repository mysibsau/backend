from django.test import TestCase
import api.models as models
from django.urls import reverse


class GroupViewTest(TestCase):
    @classmethod
    def setUp(cls):
        models.Group.objects.create(
            name='group',
            mail='group@sibsau.ru'
        )
    
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/groups/')
        self.assertEqual(resp.status_code, 200)

    def test_response_is_json(self):
        resp = self.client.get('/groups/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.accepted_media_type, 'application/json')


class PlaceViewTest(TestCase):
    @classmethod
    def setUp(cls):
        models.Place.objects.create(name='Н317')
    
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/places/')
        self.assertEqual(resp.status_code, 200)

    def test_response_is_json(self):
        resp = self.client.get('/places/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.accepted_media_type, 'application/json')


class ProfessorViewTest(TestCase):
    @classmethod
    def setUp(cls):
        models.Professor.objects.create(
            name='Фамилия Имя Отчество',
            mail='fio@sibsau.ru',
            phone='+79631859823',
            department='ИИТК'
        )
    
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/professors/')
        self.assertEqual(resp.status_code, 200)

    def test_response_is_json(self):
        resp = self.client.get('/professors/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.accepted_media_type, 'application/json')


class TimetableGroupViewTest(TestCase):
    @classmethod
    def setUp(cls):
        models.TimetableGroup.objects.create(
            even_week=True,
            day=0,
            group=models.Group.objects.create(name='БПИ18-01')
        )
    
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/timetable/group/1/0')
        self.assertEqual(resp.status_code, 200)

    def test_response_is_json(self):
        resp = self.client.get('/timetable/group/1/0')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.accepted_media_type, 'application/json')

    
class TimetablePlaceViewTest(TestCase):
    @classmethod
    def setUp(cls):
        models.TimetablePlace.objects.create(
            even_week=True,
            day=0,
            place=models.Place.objects.create(name='Н317')
        )
    
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/timetable/place/1/0')
        self.assertEqual(resp.status_code, 200)

    def test_response_is_json(self):
        resp = self.client.get('/timetable/place/1/0')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.accepted_media_type, 'application/json')

    
class TimetableProfessorViewTest(TestCase):
    @classmethod
    def setUp(cls):
        models.TimetableProfessor.objects.create(
            even_week=True,
            day=0,
            professor=models.Professor.objects.create(name='ФИО')
        )
    
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/timetable/professor/1/0')
        self.assertEqual(resp.status_code, 200)

    def test_response_is_json(self):
        resp = self.client.get('/timetable/professor/1/0')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.accepted_media_type, 'application/json')
