# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-24 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0005_auto_20160924_1514'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thing',
            new_name='Profile',
        ),
    ]
