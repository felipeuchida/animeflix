# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_episode_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='link_video',
            field=models.CharField(default='', max_length=1000),
        ),
    ]