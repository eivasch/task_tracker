# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20180619_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdescription',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='description', to='tasks.Task'),
        ),
    ]
