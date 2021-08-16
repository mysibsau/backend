from apps.support import models
from rest_framework import serializers, fields


class FAQReadSerializer(serializers.ModelSerializer):
    theme = fields.CharField(source='theme.title', label='Название темы')

    class Meta:
        model = models.FAQ
        fields = ('id', 'question', 'theme', 'answer', 'views', 'is_public', 'create_data')
        read_only_fields = fields


class FAQCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ('question', 'theme', 'is_public')


class ThemeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theme
        fields = ('slug', 'title')
