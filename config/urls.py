from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("places.urls")),
    path('', lambda res: HttpResponse(status=200,
                                      content='<ul><li><a href="/api/v1/schema/swagger-ui/">SwaggerUI</a></li>\
                                      <li><a href="/api/v1/schema/redoc/">ReDoc examples</a></li></ul>'
                                      ), name='homepage'),
]

urlpatterns += [
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token/blacklist/", TokenBlacklistView.as_view(), name='token_blacklist'),
]

urlpatterns += [
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/v1/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns += [
    path("api/v1/", include("employees.urls"),)
]