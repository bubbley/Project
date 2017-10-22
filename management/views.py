from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import RequestContext
from main.models import Project

# Create your views here.
def index(request):
    return render(request, 'mangement/index.html', None, RequestContext(request))
