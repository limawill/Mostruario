# Generated by Django 3.1.6 on 2021-07-12 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20210709_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]