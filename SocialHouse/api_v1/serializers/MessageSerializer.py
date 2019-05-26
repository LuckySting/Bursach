from rest_framework import serializers
from dbapp.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    posted = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
