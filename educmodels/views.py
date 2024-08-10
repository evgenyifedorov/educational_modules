from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
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
        if IsModerator().has_permission(self.request, self):
            return EduModel.objects.all()
        else:
            return EduModel.objects.filter(owner=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "list", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        if self.action == "create":
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        if self.action == "destroy":
            self.permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
        return super().get_permissions()


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
