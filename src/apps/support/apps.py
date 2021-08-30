from django.apps import AppConfig


class SupportConfig(AppConfig):
    name = 'apps.support'
    verbose_name = 'Помощь'

    def ready(self) -> None:
        from apps.support import models
        from apps.notifications.services.notifications_proscessor import Listener

        Listener(model=models.FAQ)
