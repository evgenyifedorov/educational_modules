from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
                  path("api/token/", TokenObtainPairView.as_view(permission_classes=[AllowAny]), name="token_obtain_pair"),
                  path("api/token/refresh/", TokenRefreshView.as_view(permission_classes=[AllowAny]), name="token_refresh"),
              ] + router.urls

