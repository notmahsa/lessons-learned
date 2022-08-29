# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import NewLessonForm, NewProjectForm
from .models import Project, LessonLearned, Account


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/new-lesson.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
@require_http_methods(["GET"])
def get_project(_, project_id=None):
    # template_name = 'home/project.html'
    project = get_object_or_404(Project, project_id)
    data = serializers.serialize('json', {"project": project})
    return HttpResponse(data, content_type='application/json')


@login_required(login_url="/login/")
@require_http_methods(["GET"])
def get_lesson(_, lesson_id=None):
    # template_name = 'home/lesson.html'
    lesson = get_object_or_404(Project, lesson_id)
    data = serializers.serialize('json', {"lesson": lesson})
    return HttpResponse(data, content_type='application/json')


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def lessons(request, lesson_id=None):
    msg = None
    success = False
    form_class = NewLessonForm()
    template_name = 'home/new-lesson.html'
    current_user = request.user
    account = Account.objects.get(user=current_user)

    if request.method == "GET" and lesson_id is not None:
        try:
            form_class = LessonLearned.objects.get(id=lesson_id)
            success = True
        except LessonLearned.DoesNotExist:
            success = False
            msg = 'Lesson does not exist'

    if request.method == "POST":
        form_class = NewLessonForm(request.POST)
        if form_class.is_valid():
            lesson = form_class.save(commit=False)
            lesson.author = account
            lesson.save()
            form_class = lesson
            msg = 'Lesson successfully created'
            success = True
        else:
            msg = form_class.errors
            success = False

    return render(request, template_name, {
        "lesson": form_class,
        "msg": msg,
        "success": success
    })


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def report(request):
    template_name = 'home/ui-report.html'
    current_user = request.user
    account = Account.objects.get(user=current_user)
    lesson_list = LessonLearned.objects.filter(author=account)

    return render(request, template_name, {
        "lessons": lesson_list,
    })


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def projects(request, project_id=None):
    msg = None
    success = True
    selected = NewProjectForm()
    template_name = 'home/ui-projects.html'
    if request.method == "GET" and project_id is not None:
        try:
            selected = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            success = False
            msg = 'Selected project does not exist'

    if request.method == "POST":
        selected = NewProjectForm(request.POST)
        if selected.is_valid():
            selected.save()
            msg = 'Project successfully updated'
            success = True
        else:
            msg = selected.errors
            success = False

    return render(request, template_name, {
        "project_list": Project.objects.all(),
        "selected": selected,
        "msg": msg,
        "success": success
    })


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def create_project(request):
    msg = None
    success = False
    project = NewProjectForm()
    template_name = 'home/ui-project.html'

    if request.method == "POST":
        project = NewProjectForm(request.POST)
        if project.is_valid():
            project.save()
            msg = 'Project successfully saved'
            success = True
        else:
            msg = project.errors
            success = False

    return render(request, template_name, {
        "project": project,
        "msg": msg,
        "success": success
    })
