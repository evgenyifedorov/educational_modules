from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class EduModel(models.Model):
    """
    Модель обучения.
    """
    number = models.IntegerField(unique=True, db_index=True, verbose_name='Номер модели')
    name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='Название модели')
    description = models.TextField(verbose_name='Описание модели')
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        **NULLABLE,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['number',]


class Lesson(models.Model):
    """
    Урок обучения.
    """
    title = models.CharField(max_length=150, verbose_name="название")
    content = models.TextField(verbose_name="описание")
    url = models.URLField(verbose_name="ссылка на урок", **NULLABLE)
    model = models.ForeignKey(EduModel, verbose_name="курсы", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        **NULLABLE,
    )
    amount = models.PositiveIntegerField(verbose_name="стоимость урока", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
