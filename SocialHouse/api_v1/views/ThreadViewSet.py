from rest_framework import generics
from ..serializers.ThreadSerializer import ThreadSerializer
from dbapp.models import Thread


class ThreadListView(generics.ListAPIView):
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()
    pagination_class = None
