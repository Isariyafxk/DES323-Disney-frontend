# Generated by Django 4.1.13 on 2023-11-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("disneyland", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="disneylandReview",
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
                ("Review_ID", models.IntegerField()),
                ("Rating", models.IntegerField()),
                ("Year", models.IntegerField()),
                ("Text", models.CharField(max_length=255)),
                ("Branch", models.CharField(max_length=255)),
            ],
        ),
    ]
