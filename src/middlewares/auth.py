from django.http import JsonResponse

from apps.user.models import User


def auth_header(get_response):
    def middleware(request):
        user_token = request.headers.get("Authorization")

        request.student = None

        if not user_token:
            return get_response(request)

        token_type, token = user_token.split()

        if token_type != 'Bearer':
            return get_response(request)

        user = User.objects.filter(token=token).first()

        if not user:
            return JsonResponse({'error': 'user not found'}, status=405)
        if user.banned:
            return JsonResponse({'error': 'you are banned'}, status=405)

        request.student = user

        return get_response(request)

    return middleware


def auth_query(get_response):
    def middleware(request):
        if request.student:
            return get_response(request)

        token = request.GET.get("token")

        if not token:
            return get_response(request)

        user = User.objects.filter(token=token).first()

        if not user:
            return JsonResponse({'error': 'user not found'}, status=405)
        if user.banned:
            return JsonResponse({'error': 'you are banned'}, status=405)

        request.student = user

        return get_response(request)

    return middleware
