from apps.support import models
from rest_framework import serializers


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ('id', 'question', 'answer', 'views')
