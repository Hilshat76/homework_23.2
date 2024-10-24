from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукт",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="catalog/products_photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Введите стоимость продукта"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        blank=True,
        null=True,
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        blank=True,
        null=True,
        help_text="Укажите дату последнего изменения",
    )
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.SET_NULL, **NULLABLE)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("category", "name",)
        permissions = [
            ("can_edit_is_active", "Can edit is_active"),
            ("can_edit_description", "Can edit description"),
            ("can_edit_category", "Can edit category")
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, verbose_name="Продукт")
    version_number = models.IntegerField(verbose_name="Номер версии")
    version_name = models.CharField(verbose_name="Название версии", max_length=150)
    is_active = models.BooleanField(verbose_name="Признак текущей версии")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f'{self.version_number} - {self.version_name}'
