# Generated by Django 5.1.1 on 2025-03-11 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trainee", "0005_alter_course_trainee_user_trainee_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trainee",
            name="user",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
