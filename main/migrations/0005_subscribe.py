# Generated by Django 4.2.6 on 2023-10-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_game_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscribe",
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
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
            ],
            options={
                "verbose_name_plural": "Subsribe",
            },
        ),
    ]