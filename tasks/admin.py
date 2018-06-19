# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from tasks.models import Task, TaskDescription


class TaskAdmin(admin.ModelAdmin):
    pass


class TaskDescriptionAdmin(admin.ModelAdmin):
    pass


admin.register(Task, TaskAdmin)
admin.register(TaskDescription, TaskDescriptionAdmin)
