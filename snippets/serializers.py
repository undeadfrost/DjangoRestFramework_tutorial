from rest_framework import serializers, permissions
from django.contrib.auth.models import User
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
