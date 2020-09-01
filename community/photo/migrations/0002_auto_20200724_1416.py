# Generated by Django 2.0.13 on 2020-07-24 05:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='list_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
