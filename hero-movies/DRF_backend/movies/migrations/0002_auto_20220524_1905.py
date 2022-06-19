# Generated by Django 3.2.12 on 2022-05-24 10:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-release_date']},
        ),
        migrations.AlterField(
            model_name='movie',
            name='voted_users',
            field=models.ManyToManyField(null=True, through='movies.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='wishing_users',
            field=models.ManyToManyField(null=True, related_name='wished_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
