# Generated by Django 3.2.3 on 2021-11-21 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='liked',
        ),
    ]