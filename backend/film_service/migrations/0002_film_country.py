# Generated by Django 4.1.2 on 2023-05-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("film_service", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="country",
            field=models.CharField(default="UNKNOWN", max_length=50),
        ),
    ]