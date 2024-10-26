# Generated by Django 5.1 on 2024-10-04 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
    ]
