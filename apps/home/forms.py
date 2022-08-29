# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from localflavor.us.forms import USStateField

from .models import LessonLearned, Project


class NewLessonForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 30, "cols": 100}))
    project = forms.ModelChoiceField(Project.objects.all(), empty_label=None)

    class Meta:
        model = LessonLearned
        fields = "__all__"


class NewProjectForm(forms.ModelForm):
    state = USStateField(empty_label=None)

    class Meta:
        model = Project
        fields = "__all__"
