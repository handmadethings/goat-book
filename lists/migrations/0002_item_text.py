# Generated by Django 5.1.4 on 2025-01-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="text",
            field=models.TextField(default=""),
        ),
    ]
