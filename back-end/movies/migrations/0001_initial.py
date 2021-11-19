# Generated by Django 3.2.3 on 2021-11-19 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('vote', models.FloatField()),
                ('country', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=10)),
                ('poster_path', models.TextField()),
                ('actor_1', models.CharField(max_length=20)),
                ('actor_2', models.CharField(default='', max_length=20)),
                ('actor_3', models.CharField(default='', max_length=20)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField(default='')),
                ('content', models.TextField()),
                ('genre', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.FloatField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
