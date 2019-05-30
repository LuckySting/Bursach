from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .TokenSettings import *
from .views.ThreadViewSet import *
from .views.ArticleViewSet import *
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('auth', TokenObtainPairViewMod.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('thread/list', ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:thread__id>/article/list', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleViewSet.as_view(), name='article_rd'),
    path('article', ArticleCreateView.as_view(), name='article_c'),
    path('docs/', include_docs_urls(title='API v1 docs', permission_classes=(AllowAny,)))
]
