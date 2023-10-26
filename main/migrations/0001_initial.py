# Generated by Django 4.2.6 on 2023-10-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                (
                    "img",
                    models.ImageField(upload_to="media", verbose_name="Game Image"),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Name of the game"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Game Price"
                    ),
                ),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="Price Discount"
                    ),
                ),
                ("about", models.TextField(verbose_name="About Game")),
                ("gameID", models.CharField(max_length=15, verbose_name="Game ID")),
                ("genre", models.CharField(max_length=50, verbose_name="Ganre")),
                (
                    "multi_tags",
                    models.CharField(max_length=50, verbose_name="Multy tags"),
                ),
            ],
            options={
                "verbose_name": "Game",
                "verbose_name_plural": "Games",
            },
        ),
    ]
