# Generated by Django 5.1.1 on 2025-03-11 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainee", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="courses",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trainee.trainee",
            ),
        ),
    ]
