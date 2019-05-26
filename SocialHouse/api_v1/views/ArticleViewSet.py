from rest_framework import generics
from ..serializers.ArticleSerializer import ArticleSerializer
from ..serializers.ArticleSerializer import ArticleDetailSerializer
from dbapp.models import Article


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    lookup_url_kwarg = 'brunch__pk'

    def get_queryset(self):
        brunch__id = self.kwargs.get(self.lookup_url_kwarg)
        return Article.objects.filter(brunch__id=brunch__id)


class ArticleViewSet(generics.RetrieveDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()