from django.contrib import admin

from educmodels.models import Lesson, EduModel


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )


@admin.register(EduModel)
class EduModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
