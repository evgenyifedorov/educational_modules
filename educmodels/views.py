from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from educmodels.models import EduModel, Lesson

from educmodels.pagination import EduModelPagination
from educmodels.serializers import LessonSerializer, EduModelSerializer
from educmodels.permissions import IsModerator, IsOwner


class EduModelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for EduModel
    """

    queryset = EduModel.objects.all()
    serializer_class = EduModelSerializer
    pagination_class = EduModelPagination

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_queryset(self):
        """
        Return a queryset of EduModel objects for the current user,
        or all EduModel objects if the user is a moderator.
        """
        if IsModerator().has_permission(self.request, self):
            return EduModel.objects.all()
        else:
            return EduModel.objects.filter(owner=self.request.user)


class LessonCreateAPIView(CreateAPIView):
    """
    Lesson create endpoint
    """

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """
    Lesson list endpoint
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = EduModelPagination

    def get_queryset(self):
        """
        Return a queryset of Lesson objects for the current user,
        or all Lesson objects if the user is a moderator.
        """
        if IsModerator().has_permission(self.request, self):
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    Lesson retrieve endpoint
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(UpdateAPIView):
    """
    Lesson update endpoint
    """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    """
    Lesson destroy endpoint
    """

    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
