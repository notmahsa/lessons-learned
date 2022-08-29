# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import uuid

from django.contrib.auth.models import User
from localflavor.us.us_states import STATE_CHOICES

from apps.home.config import *


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clark_id = models.CharField(max_length=6, unique=True, null=True)
    budget = models.FloatField(default=0.)
    title = models.CharField(max_length=30, unique=True)
    division = models.CharField(
        max_length=50,
        choices=ProjectDivision.choices,
        null=True
    )
    delivery_method = models.CharField(
        max_length=50,
        choices=ProjectDeliveryMethod.choices,
        null=True
    )
    client = models.CharField(max_length=30, null=True)
    venture = models.CharField(max_length=30, null=True)
    structure = models.CharField(
        max_length=50,
        choices=ProjectStructure.choices,
        null=True
    )
    due = models.DateField(null=True)
    ntp = models.CharField(max_length=30, null=True)
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        null=True
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='projects')

    def __str__(self):
        return "%s: %s" % (self.clark_id, self.title)


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='accounts')

    def __str__(self):
        return self.user.username


class LessonLearned(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='lessons')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(unique=True, null=True, blank=True, max_length=30)
    body = models.TextField(null=True, blank=True)
    permission_level = models.CharField(
        max_length=50,
        choices=PermissionLevel.choices,
        default=PermissionLevel.PRIVATE,
        blank=True,
    )
    project_phase = models.CharField(
        max_length=50,
        choices=LessonProjectPhase.choices,
        default=LessonProjectPhase.INITIAL,
    )
    category = models.CharField(
        max_length=50,
        choices=LessonCategory.choices,
        null=True,
        blank=True
    )
    impact = models.CharField(
        max_length=50,
        choices=LessonImpact.choices,
        null=True,
        blank=True
    )
    is_editable = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50,
        choices=LessonReportStatus.choices,
        default=LessonReportStatus.DRAFT,
        blank=True,
    )

    def __str__(self):
        return self.title
