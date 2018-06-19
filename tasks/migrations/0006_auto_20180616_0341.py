# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-16 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20180616_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AddField(
            model_name='taskdescription',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='description', to='tasks.Task'),
        ),
    ]