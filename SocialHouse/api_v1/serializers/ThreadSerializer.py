from rest_framework import serializers
from dbapp.models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
