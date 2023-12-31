# Generated by Django 4.1.13 on 2023-11-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("models", "0002_delete_disneylandreview"),
    ]

    operations = [
        migrations.CreateModel(
            name="DisneylandReview",
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
                ("Review_ID", models.CharField(max_length=10)),
                ("Rating", models.IntegerField()),
                ("Year", models.CharField(max_length=10)),
                ("Text", models.CharField(max_length=1000)),
                ("Branch", models.CharField(max_length=255)),
            ],
        ),
    ]
