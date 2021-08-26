from rest_framework.generics import ListAPIView

from apps.campus_sibsau import models
from apps.campus_sibsau.api.v3 import serializers


class SportClubsAPIView(ListAPIView):
    queryset = models.SportClub.objects.all()
    serializer_class = serializers.SportClubSerializer
