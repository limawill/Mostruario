# Generated by Django 3.2.5 on 2021-07-12 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0004_auto_20210712_1243"),
    ]

    operations = [
        migrations.RenameField(
            model_name="photo",
            old_name="image",
            new_name="image",
        ),
    ]
