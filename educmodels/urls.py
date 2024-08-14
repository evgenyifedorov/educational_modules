from django.urls import path
from rest_framework.routers import DefaultRouter

from educmodels.apps import EducmodelsConfig
from educmodels.views import (
    EduModelViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
)

app_name = EducmodelsConfig.name

router = DefaultRouter()
router.register(r"educmodels", EduModelViewSet, basename="educmodels")
urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="create_lesson"),
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="update_lesson"
    ),
    path(
        "lesson/retrieve/<int:pk>/",
        LessonRetrieveAPIView.as_view(),
        name="retrieve_lesson",
    ),
    path(
        "lesson/destroy/<int:pk>/",
        LessonDestroyAPIView.as_view(),
        name="destroy_lesson",
    ),
] + router.urls
