# Generated by Django 5.1 on 2024-09-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_car_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carbrand",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="cars/brands/"),
        ),
    ]
