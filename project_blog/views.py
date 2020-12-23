from django.shortcuts import render

from project_blog.models import Project
from django.conf import settings

def project_index(request):

    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)



def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)
