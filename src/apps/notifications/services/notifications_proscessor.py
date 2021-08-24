from django.db.models.base import ModelBase
from django.db.models.signals import post_save
from typing import List
from constance import config
from requests import post as post_request
from ..models import Notifications


class NotificationProcessor:
    HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {config.FIREBASE_TOKEN}',
    }

    def __init__(self, user) -> None:
        self.user = user

    def send(self, title: str, text: str, click_action: str) -> None:
        json = self.generate_json(title, text, click_action)
        print(json)
        response = post_request("https://fcm.googleapis.com/fcm/send", headers=self.HEADERS, json=json)
        print(response.text)

    def generate_json(self, title, text, click_action) -> dict:
        return {
            'notification': {
                'title': title,
                'body': text,
            },
            'data': {
                'click_action': click_action,
            },
            'to': f'/topics/{self.user.token}',
        }


class Listener:
    def __init__(self, model: Notifications):
        post_save.connect(self, sender=model)

    def __call__(self, update_fields, instance: Notifications, **kwargs):
        if not update_fields:
            return

        user = getattr(instance, instance.USER_FIELD)

        for field in instance.FIELDS:
            if field in update_fields:
                NotificationProcessor(user).send(
                    instance.TITLE,
                    getattr(instance, field),
                    instance.CLICK_ACTION,
                )
                return
