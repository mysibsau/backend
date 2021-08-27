from rest_framework.authentication import BaseAuthentication
from apps.user.models import User


class TwoBearerTokenAuthentication(BaseAuthentication):
    def get_token(self, request) -> str:
        """Получение токена либо из заголовков, либо из get параметров"""
        if token := request.GET.get('token'):
            return token
        auth = request.headers.get('Authorization')
        if not auth:
            return None
        type_auth, token = auth.split()
        if type_auth != 'Bearer':
            return None
        return token

    def authenticate(self, request):
        token = self.get_token(request)

        if not token:
            return None

        if user := User.objects.filter(token=token).first():
            return (user, None)
        if user := User.objects.filter(auth_token__key=token).first():
            return (user, None)

    def get_user(self, user_id):
        return User.objects.filter(pk=user_id).first()
