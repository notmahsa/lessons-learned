# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.apps import AppConfig
from django.db import models


class MyConfig(AppConfig):
    name = 'apps.home'
    label = 'apps_home'


class LessonProjectPhase(models.TextChoices):
    INITIAL = 'Initial (Precon)'
    PLAN = 'Planning/Execution'
    CLOSE_OUT = 'Close out'


class PermissionLevel(models.TextChoices):
    PRIVATE = 'Private'
    PROJECT = 'Project'
    PUBLIC = 'Public'


class LessonImpact(models.TextChoices):
    POSITIVE = 'Positive'
    MODERATE = 'Moderate'
    NEGATIVE = 'Negative'


class LessonCategory(models.TextChoices):
    MARKETING = 'Marketing/Pursuing (Bid/Legal)'
    BUSINESS = 'Purchasing/Business Management'
    HR = 'HR/Team Setup'
    PERMIT = 'Mobilization/Permit'
    SAFETY = 'Safety'
    QC = 'QC'
    SCHEDULING = 'Scheduling'
    SC = 'Procurement/Supply Chain/Inflation'
    CHANGE_ORDER = 'Change Order Management'
    STAKEHOLDER_MGT = 'Stakeholder Management'
    DOC_MGT = 'Document Control Management'
    PO = 'Punch Out'


class LessonReportStatus(models.TextChoices):
    DRAFT = 'Draft'
    PENDING_REVIEW = 'Pending Review'
    APPROVED = 'Approved'
    CHANGE_REQUESTED = 'Change Requested'
    REJECTED = 'Rejected'


class ProjectDivision(models.TextChoices):
    BASE = 'Clark Base'
    CIVIL = 'Clark Civil'
    FOUNDATION = 'Clark Foundation'
    WATER = 'Clark Water'
    CONCRETE = 'Clark Concrete'
    C3M = 'C3M'
    ATKINSON = 'Atkinson'
    SHIRLEY = 'Shirley'
    CODA = 'CODA'
    CARTA = 'CARTA'


class ProjectDeliveryMethod(models.TextChoices):
    DBBUILD = 'Design-Bid-Build'
    DBUILD = 'Design-Build'
    CMAR = 'Construction Manager at Risk (CMAR)'


class ProjectStructure(models.TextChoices):
    PEMB = 'PEMB'
    STEEL = 'Steel'
    CONCRETE = 'Concrete'
    COMPOSITE = 'Composite'
    UU = 'Underground Utility'
    TUNNEL = 'Tunneling'
    SHEET = 'Sheeting/Shoring'
    PROCP = 'Process Piping'
    BRIDGE = 'Bridge'
    ROAD = 'Road'
