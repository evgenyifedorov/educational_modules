from rest_framework.serializers import ModelSerializer
from educmodels.models import EduModel, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class EduModelSerializer(ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True, source="lesson_set")

    class Meta:
        model = EduModel
        fields = "__all__"
