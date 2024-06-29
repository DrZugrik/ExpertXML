# Generated by Django 5.0.2 on 2024-06-29 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0007_alter_uploadedfile_file"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "verbose_name": "Профиль пользователя",
                "verbose_name_plural": "Профили пользователей",
            },
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="date_added",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="document",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="xml_data",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="company",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Организация"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="date_birth",
            field=models.DateField(blank=True, null=True, verbose_name="Дата рождения"),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.date.today, verbose_name="Дата регистрации"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Имя"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="groups",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Группы"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Отчество"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="user_photos/", verbose_name="Фото"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="surname",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Фамилия"
            ),
        ),
    ]