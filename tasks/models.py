# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    project = models.CharField(max_length=256)
    status = models.CharField(max_length=50,
                              choices=(('Created', 'Created'),
                                       ('In progress', 'In progress'),
                                       ('Done', 'Done'))
                              )
    performer = models.CharField(max_length=256)
    author = models.CharField(max_length=256)


class TaskDescription(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, related_name='description', null=True)
