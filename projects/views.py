from django.shortcuts import render

from django.http import HttpResponse

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
    msg = "Hello You are on message page"
    num = 10
    context = {'msg':msg,'age':num}
    return render(request, 'projects/projects.html',{'projects':project_list})

def project(request, pk):
    projectOBJ = None
    for i in project_list:
        if i['id'] == int(pk):
            projectOBJ = i
    return render(request, 'projects/single-projects.html',{'project':projectOBJ})