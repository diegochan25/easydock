from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods
from apps.core.models import SampleWord
from apps.projects.forms import CreateProject
from apps.projects.models import Project
from apps.core.types import AppHttpRequest
from apps.services.catalog import DATABASES, RUNTIMES
from apps.services.forms import CreateDatabaseService, CreateFunctionService


@login_required
@require_http_methods(['GET', 'POST'])
def index(request: AppHttpRequest):
    projects = []
    match (request.method):
        case 'GET':
            form = CreateProject(initial={'project_name': SampleWord.random_name()})
        case 'POST':
            form = CreateProject(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                project = Project(
                    name=data['project_name'], 
                    description=data.get('description'),
                    creator=request.user,
                    owner=request.user
                )
                project.save()
                return redirect('projects:show', id=project.id)

    return render(request, 'projects/index.html.j2', {
        'projects': projects,
        'form': form, 
    })

@login_required
@require_http_methods(['GET'])
def show(request: AppHttpRequest, id: int):
    project =  get_object_or_404(Project, id=id)
    database_form = CreateDatabaseService()
    function_form = CreateFunctionService()
    return render(request, 'projects/show.html.j2', { 
        'project': project,
        'database_form': database_form,
        'function_form': function_form,
        'databases': DATABASES,
        'runtimes': RUNTIMES,
    })