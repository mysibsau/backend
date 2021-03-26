from django.test import TestCase
from django.urls import reverse
from django.test import Client
import datetime


class CriticalWayTestMenu(TestCase):
    def setUp(self):
        self.client = Client()

    def test_all_menu(self):
        url = reverse('menu_all')
        response = self.client.get(url)
        result = response.json()
        if datetime.datetime.today().weekday() == 6:
            assert result.get('error') == 'menu is empty'
        else:
            assert len(result) > 0
