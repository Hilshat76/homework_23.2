# Generated by Django 5.1 on 2024-10-17 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                    "username",
                    models.CharField(
                        help_text="Введите имя пользователя",
                        max_length=50,
                        verbose_name="Имя пользователя",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="article/avatar",
                        verbose_name="Аватар пользователя",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите электронную почту",
                        max_length=254,
                        unique=True,
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="Страна"
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Article",
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
                    "title",
                    models.CharField(
                        help_text="Введите заголовок статьи",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="slug"
                    ),
                ),
                ("content", models.TextField(verbose_name="содержимое")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="article/article_preview",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "sign_of_publication",
                    models.BooleanField(
                        default=True, verbose_name="признак публикации"
                    ),
                ),
                (
                    "number_of_views",
                    models.PositiveIntegerField(
                        default=0, verbose_name="количество просмотров"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="articles",
                        to="article.user",
                        verbose_name="Автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "статья",
                "verbose_name_plural": "статьи",
            },
        ),
    ]