# Generated by Django 3.2.5 on 2021-07-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20210712_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
