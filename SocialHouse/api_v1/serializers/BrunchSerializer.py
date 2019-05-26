from rest_framework import serializers
from dbapp.models import Brunch


class BrunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brunch
        fields = '__all__'
