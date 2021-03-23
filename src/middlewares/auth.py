from apps.user.models import User
import json


def auth(get_response):
    def middleware(request):
        user_token = request.GET.get("token")
        response = get_response(request)

        if not user_token:
            return response

        user = User.objects.filter(token=user_token).first()

        if not user:
            response.data = {'error': 'user not found'}
            response.content = json.dumps(response.data)
        elif user.banned:
            response.data = {'error': 'you are banned'}
            response.content = json.dumps(response.data)
        else:
            request.GET['student'] = user
        return response

    return middleware
