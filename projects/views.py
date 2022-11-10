from django.shortcuts import render

from django.http import HttpResponse
from .models import Project

project_list = [
    {'id':1,
    'name':'vick',
    'age':10,
    'title':'ok'},
    {'id':2,
    'name':'rake',
    'age':15,
    'title':'nook'},
    {'id':3,
    'name':'kate',
    'age':102,
    'title':'okkk'}
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html',context)

def project(request, pk):
    projectOBJ = Project.objects.get(id=pk)
    tags = projectOBJ.tags.all()
    return render(request, 'projects/single-projects.html',{'projectOBJ':projectOBJ,'tags':tags})