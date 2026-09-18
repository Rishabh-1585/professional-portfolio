from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()

    return render(request, "projects.html", {
        "projects": projects
    })


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)

    return render(request, "project_detail.html", {
        "project": project
    })