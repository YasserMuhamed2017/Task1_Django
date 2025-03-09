# Generated by Django 5.1.1 on 2025-03-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course", models.CharField(max_length=100)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Trainee",
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
                ("trainee", models.CharField(max_length=100)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]
