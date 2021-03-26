from django.test import TestCase
from django.urls import reverse
from django.test import Client
from time import time
from apps.informing import models
from datetime import datetime


def test_rps(url, method) -> float:
    start_time = time()
    for _ in range(3000):
        method(url)
    return 3000 / (time() - start_time)


class LoadTestingInformin(TestCase):
    def setUp(self):
        self.client = Client()
        models.News.objects.create(
            author='test',
            text='test',
            date_to=datetime(2024, 2, 2),
        )

    def test_all_events(self):
        url = reverse('informing_all_events')
        rps = test_rps(url, self.client.get)
        assert rps > 25

    def test_all_news(self):
        url = reverse('informing_all_news')
        rps = test_rps(url, self.client.get)
        assert rps > 25

    def test_like(self):
        url = reverse('informing_like', args=[0])
        rps = test_rps(url, self.client.post)
        assert rps > 25

    def test_view(self):
        url = reverse('informing_view', args=[0])
        rps = test_rps(url, self.client.post)
        assert rps > 25
