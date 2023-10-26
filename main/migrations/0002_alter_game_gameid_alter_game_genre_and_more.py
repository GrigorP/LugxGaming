# Generated by Django 4.2.6 on 2023-10-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="gameID",
            field=models.CharField(blank=True, max_length=15, verbose_name="Game ID"),
        ),
        migrations.AlterField(
            model_name="game",
            name="genre",
            field=models.CharField(blank=True, max_length=50, verbose_name="Ganre"),
        ),
        migrations.AlterField(
            model_name="game",
            name="multi_tags",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Multy tags"
            ),
        ),
    ]