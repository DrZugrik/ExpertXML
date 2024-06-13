# Generated by Django 5.0.2 on 2024-02-09 15:49

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bootstrap_test", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AI_Models",
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
                    "name",
                    models.CharField(
                        blank=True, max_length=1000, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Короткое название",
                    ),
                ),
                (
                    "mission",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Назначение",
                    ),
                ),
                (
                    "link_github",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Ссылка на github",
                    ),
                ),
                (
                    "ai_model",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="ai_model/",
                        verbose_name="Ссылка для загрузки",
                    ),
                ),
                (
                    "version",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Версия XML"
                    ),
                ),
                (
                    "date_public",
                    models.DateField(
                        default=datetime.date.today, verbose_name="Дата публикации"
                    ),
                ),
                (
                    "date_upload",
                    models.DateField(
                        default=datetime.date.today,
                        verbose_name="Дата загрузки на сайт",
                    ),
                ),
                (
                    "date_unused",
                    models.DateField(
                        default=datetime.date.today,
                        verbose_name="Дата прекращения использования",
                    ),
                ),
            ],
            options={
                "verbose_name": "Нейросеть для преобразования",
                "verbose_name_plural": "Нейросети для преобразования",
            },
        ),
        migrations.AlterModelOptions(
            name="xmlschema",
            options={"verbose_name": "XML схема", "verbose_name_plural": "XML схемы"},
        ),
        migrations.RemoveField(
            model_name="xmlschema",
            name="file",
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="date_public",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Дата публикации"
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="date_unused",
            field=models.DateField(
                default=datetime.date.today,
                verbose_name="Дата прекращения использования",
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="date_upload",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Дата загрузки на сайт"
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="file_annot",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="xml_schemas/",
                verbose_name="Файл аннотации",
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="file_schem",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="xml_schemas/",
                verbose_name="Файл XML схемы",
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="link",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Ссылка"
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="normative",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Норматив"
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="short_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Короткое название"
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="stage",
            field=models.CharField(
                choices=[
                    ("building", "Этап проектирования"),
                    ("exploitation", "Этап строительства"),
                ],
                max_length=20,
                null=True,
                verbose_name="Этап",
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="version",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Версия XML"
            ),
        ),
        migrations.AlterField(
            model_name="xmlschema",
            name="name",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Название"
            ),
        ),
        migrations.AddField(
            model_name="xmlschema",
            name="ai_model",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bootstrap_test.ai_models",
                verbose_name="Модель для преобразования",
            ),
        ),
    ]
