from django.utils.datetime_safe import datetime
from rest_framework import generics
from ..serializers.ArticleSerializer import ArticleSerializer
from ..serializers.ArticleSerializer import ArticleDetailSerializer
from dbapp.models import Article


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'thread__id'

    def get_queryset(self):
        thread__id = self.kwargs.get(self.lookup_url_kwarg)
        return Article.objects.filter(thread__id=thread__id)


class ArticleViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, posted=datetime.now())
