from apps.support import models
from rest_framework import serializers, fields


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ('id', 'question', 'theme', 'answer', 'views', 'is_public')


class ThemeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theme
        fields = ('slug', 'title', )
