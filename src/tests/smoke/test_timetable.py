from django.test import TestCase
from django.urls import reverse
from django.test import Client
from random import randint


class SmokeTestTimetable(TestCase):
    def setUp(self):
        self.client = Client()

    def test_all_groups(self):
        url = reverse('timetable_all_groups')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_all_teachers(self):
        url = reverse('timetable_all_teachers')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_all_places(self):
        url = reverse('timetable_all_places')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_groups_hash(self):
        url = reverse('timetable_groups_hash')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_teachers_hash(self):
        url = reverse('timetable_teachers_hash')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_places_hash(self):
        url = reverse('timetable_places_hash')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_group_timetable(self):
        url = reverse('timetable_group_timetable', args=[randint(0, 100)])
        response = self.client.get(url)
        assert response.status_code == 404

    def test_teacher_timetable(self):
        url = reverse('timetable_teacher_timetable', args=[randint(0, 100)])
        response = self.client.get(url)
        assert response.status_code == 404

    def test_place_timetable(self):
        url = reverse('timetable_place_timetable', args=[randint(0, 100)])
        response = self.client.get(url)
        assert response.status_code == 404
