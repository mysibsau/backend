from xmlrpc.client import ProtocolError

from api_pallada import API
from django.contrib.auth.backends import BaseBackend

from apps.timetable.models import Group
from apps.user.models import User
from apps.user.services.getters import get_fio_group_and_average
from apps.user.services.utils import make_token


class OdooBackend(BaseBackend):
    def get_user_from_db(self, username, password):
        if user := User.objects.filter(username=username).first():
            return user if user.check_password(password) else None

    def authenticate(self, request, username=None, password=None):
        try:
            api = API('portfolio', username, password)
            # Нужно, чтобы пользователь мог обращаться к сервисам паллады
            request.api = api
        except (ProtocolError, TimeoutError):
            # Если паллада лежит, пытаемся достать студента из бд
            return self.get_user_from_db(username, password)

        if not api.uid:
            return self.get_user_from_db(username, password)

        fio, group, average = get_fio_group_and_average(api)

        user, _ = User.objects.get_or_create(
            username=username,
        )

        user.fio = fio
        user.group = Group.objects.filter(name=group).first()
        user.token = make_token(username, uid=api.uid)
        # Чистим базу от старых пользователей
        User.objects.filter(username=user.token).delete()
        user.average = average
        user.set_password(password)
        user.save()

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
