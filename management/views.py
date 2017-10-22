from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.forms import CharField
from django.core import validators
from main.models import Project
import datetime



# Create your views here.


def index(request):
    project_list = Project.objects.order_by('-created')[:10]
    context = {'project_list' : project_list}
    return render(request, 'management/index.html', context, RequestContext(request))


def delete_project(request, projectid):
    if request.POST :
        project = get_object_or_404(Project, pk=projectid)
        project.delete()
        return redirect('management:index')
    else:
        project = get_object_or_404(Project, pk=projectid)
        context = {'project': project}
        return render(request, 'management/deleteproject.html', context, RequestContext(request))

def create_new(request):
    if request.POST :
        name = request.POST["name"]
        description = request.POST["description"]

        project = Project(name=name, description=description, calculated_due=datetime.datetime.now())
        project.save()

        return redirect('management:index')

    return render(request, 'management/newproject.html', None, RequestContext(request))

