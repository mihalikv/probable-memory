# Generated by Django 5.0.2 on 2024-02-27 19:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="question",
            new_name="author",
        ),
    ]
