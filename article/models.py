from django.db import models


NULLABLE = {"blank": True, "null": True}


class User(models.Model):
    username = models.CharField(
        max_length=50,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя",
    )
    avatar = models.ImageField(
        upload_to="article/avatar", verbose_name="Аватар пользователя", **NULLABLE
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите электронную почту",
    )
    country = models.CharField(max_length=15, verbose_name="Страна", **NULLABLE)

    def __str__(self):
        return f"{self.username} ({self.email})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Article(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок статьи"
    )
    slug = models.CharField(max_length=100, verbose_name="slug", **NULLABLE)
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(
        upload_to="article/article_preview", verbose_name="Превью", **NULLABLE
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания", **NULLABLE
    )
    sign_of_publication = models.BooleanField(
        default=True, verbose_name="признак публикации"
    )
    number_of_views = models.PositiveIntegerField(
        default=0, verbose_name="количество просмотров"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Автор",
        **NULLABLE,
        related_name="articles",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
