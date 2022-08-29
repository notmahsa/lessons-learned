# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from apps.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('report/', views.report, name="report"),
    path('lesson/', views.lessons, name="lesson"),
    path('lesson/<uuid:lesson_id>/', views.lessons, name="lesson"),
    path('projects/', views.projects, name="projects"),
    path('projects/<uuid:project_id>/', views.projects, name="projects"),
    path('create-project/', views.create_project, name="create-project"),
    path('get-lesson/<uuid:lesson_id>/', views.get_lesson, name="get-lesson"),
    path('get-project/<uuid:project_id>/', views.get_project, name="get-project"),

    # Matches any html file
    re_path(r'^.*\.html$', views.pages, name='pages'),
]
