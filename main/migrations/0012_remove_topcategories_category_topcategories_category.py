# Generated by Django 4.2.6 on 2023-10-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_topcategories_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="topcategories",
            name="category",
        ),
        migrations.AddField(
            model_name="topcategories",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topcat",
                to="main.category",
            ),
        ),
    ]
