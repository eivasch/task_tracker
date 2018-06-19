# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tasks.models import Task


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comment')
    author = models.CharField(max_length=256)
    text = models.TextField()
