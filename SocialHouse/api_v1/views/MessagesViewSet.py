from django.utils.datetime_safe import datetime
from rest_framework import generics
from ..serializers.MessageSerializer import MessageSerializer
from ..serializers.ArticleSerializer import ArticleDetailSerializer
from dbapp.models.Message import Message


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    lookup_url_kwarg = 'article__id'
    pagination_class = None

    def get_queryset(self):
        article__id = self.kwargs.get(self.lookup_url_kwarg)
        return Message.objects.filter(article__id=article__id)
