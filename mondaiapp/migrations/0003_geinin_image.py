# Generated by Django 4.1.5 on 2023-01-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mondaiapp", "0002_geinin_delete_manzai"),
    ]

    operations = [
        migrations.AddField(
            model_name="geinin",
            name="image",
            field=models.CharField(default="タイトル", max_length=20),
        ),
    ]