# Generated by Django 5.0.6 on 2024-05-19 09:00

import nav.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nav", "0008_alter_icon_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="icon",
            name="icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="icon/",
                validators=[nav.validators.validate_file_extension],
            ),
        ),
    ]
