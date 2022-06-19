# Generated by Django 3.2.12 on 2022-05-26 14:02

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220526_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, size=[300, 300], upload_to='profile_images'),
        ),
    ]