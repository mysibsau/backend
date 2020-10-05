from django.http import HttpResponse
from os import system


class BanScumbags:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if ".php" in request.get_raw_uri():
            ip = request.META.get('REMOTE_ADDR')
            system(f'ufw deny from {ip} to any')
            return HttpResponse('I fuck u', content_type="and your mom")

        response = self.get_response(request)
        return response