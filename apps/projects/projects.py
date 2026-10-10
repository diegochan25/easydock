from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from apps.core.types import AppHttpRequest
from apps.projects.models import Project


def project_required(view):
    @wraps(view)
    @login_required
    def wrapper(request: AppHttpRequest, project_id, *args, **kwargs):
        request.project = get_object_or_404(Project, id=project_id, owner=request.user)
        return view(request, *args, **kwargs)
    return wrapper
