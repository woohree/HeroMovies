# Generated by Django 3.2.12 on 2022-05-25 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='articlecommentcomment',
            options={'ordering': ['-created_at']},
        ),
    ]
