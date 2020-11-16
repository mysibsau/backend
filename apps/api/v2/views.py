from rest_framework import viewsets
from django.shortcuts import redirect


class RedirectOn(viewsets.ViewSet):
    def sibsau(self, request):
        return redirect('https://sibsau.ru/')
