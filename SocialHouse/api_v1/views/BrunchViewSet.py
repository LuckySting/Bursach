from rest_framework import generics
from ..serializers.BrunchSerializer import BrunchSerializer
from dbapp.models import Brunch


class BrunchListView(generics.ListAPIView):
    serializer_class = BrunchSerializer
    lookup_url_kwarg = 'thread__pk'

    def get_queryset(self):
        thread__id = self.kwargs.get(self.lookup_url_kwarg)
        return Brunch.objects.filter(thread__id=thread__id)
