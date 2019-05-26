from rest_framework import serializers
from dbapp.models import Article
from .MessageSerializer import MessageSerializer


class ArticleSerializer(serializers.ModelSerializer):
    messages_count = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    posted = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'name', 'posted', 'text', 'author', 'messages_count')


class ArticleDetailSerializer(serializers.ModelSerializer):
    messages_count = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    posted = serializers.DateTimeField(read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'name', 'posted', 'text', 'author', 'messages_count', 'messages')
