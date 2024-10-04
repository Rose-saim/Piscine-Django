# Generated by Django 5.1.1 on 2024-10-04 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.article"
            ),
        ),
    ]