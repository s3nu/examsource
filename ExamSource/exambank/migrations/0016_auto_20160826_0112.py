# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-26 01:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exambank', '0015_auto_20160826_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='Classes',
            new_name='classes',
        ),
    ]