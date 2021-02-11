from rest_framework.generics import ListAPIView, RetrieveAPIView

from articles.models import Article
from .serializers import ArticleSerializer


class ArticleListView(ListAPIView):
    """Get List of Arcticle Data"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    """Get Detail of Article Data based of PK"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
