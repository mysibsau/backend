from rest_framework.generics import ListAPIView

from apps.campus_sibsau import models
from api.v3.campus_sibsau import serializers


class SportClubsAPIView(ListAPIView):
    queryset = models.SportClub.objects.all()
    serializer_class = serializers.SportClubSerializer
