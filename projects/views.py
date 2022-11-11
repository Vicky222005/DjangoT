from django.shortcuts import render

from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    projectOBJ = Project.objects.get(id=pk)
    tags = projectOBJ.tags.all()
    return render(request, 'projects/single-projects.html',{'projectOBJ':projectOBJ,'tags':tags})

def createProject(request):
    form = ProjectForm()
    context = {'form':form}
    return render(request, "projects/project_form.html", context)