from django.db.models.signals import post_save
from constance import config
from requests import post as post_request
from apps.notifications.models import Notifications
from rest_framework.authtoken.models import Token


class NotificationProcessor:
    HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {config.FIREBASE_TOKEN}',
    }

    def __init__(self, user) -> None:
        self.user = user

    def send(self, title: str, text: str, click_action: str) -> None:
        json = self.generate_json(title, text, click_action)
        post_request("https://fcm.googleapis.com/fcm/send", headers=self.HEADERS, json=json)

    def generate_json(self, title, text, click_action) -> dict:
        token, _ = Token.objects.get_or_create(user=self.user)
        return {
            'notification': {
                'title': title,
                'body': text,
            },
            'data': {
                'click_action': click_action,
            },
            'to': f'/topics/{token}',
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
