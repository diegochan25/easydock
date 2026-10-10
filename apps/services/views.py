from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.core.types import AppHttpRequestWithProject
from apps.projects.projects import project_required

# Create your views here.
@project_required
@require_http_methods(['GET', 'POST'])
def index(request: AppHttpRequestWithProject):
    pass