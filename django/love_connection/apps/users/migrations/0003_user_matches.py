# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-11 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_pw_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='matches',
            field=models.ManyToManyField(related_name='_user_matches_+', to='users.User'),
        ),
    ]
