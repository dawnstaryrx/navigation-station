# Generated by Django 5.0.6 on 2024-05-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nav", "0014_alter_icon_app"),
    ]

    operations = [
        migrations.AddField(
            model_name="icon",
            name="site",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
