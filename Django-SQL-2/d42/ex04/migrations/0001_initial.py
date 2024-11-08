# Generated by Django 5.1.1 on 2024-10-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("episode_nb", models.IntegerField()),
                ("title", models.CharField(max_length=100)),
                ("director", models.CharField(max_length=100)),
                ("producer", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
            ],
        ),
    ]
