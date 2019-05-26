from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .TokenSettings import *
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('auth', TokenObtainPairViewMod.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='API v1 docs', permission_classes=(AllowAny,)))
]
