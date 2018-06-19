# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20180616_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('In progress', 'In progress'), ('Done', 'Done')], max_length=50),
        ),
        migrations.AlterField(
            model_name='taskdescription',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='description', to='tasks.Task'),
            preserve_default=False,
        ),
    ]
