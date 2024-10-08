# Generated by Django 5.0.7 on 2024-08-07 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EduModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        db_index=True, unique=True, verbose_name="Номер модели"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=30,
                        unique=True,
                        verbose_name="Название модели",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание модели")),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "Модель",
                "verbose_name_plural": "Модели",
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="название")),
                ("content", models.TextField(verbose_name="описание")),
                (
                    "url",
                    models.URLField(
                        blank=True, null=True, verbose_name="ссылка на урок"
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="стоимость урока"
                    ),
                ),
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="educmodels.edumodel",
                        verbose_name="курсы",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="владелец",
                    ),
                ),
            ],
            options={
                "verbose_name": "урок",
                "verbose_name_plural": "уроки",
            },
        ),
    ]
