from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.models import Dog


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class DogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Dog
        fields = ('id', 'name', 'created',)