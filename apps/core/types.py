from typing import TYPE_CHECKING
from django.http import HttpRequest

if TYPE_CHECKING:
    from apps.accounts.models import User
    from apps.projects.models import Project

class AppHttpRequest(HttpRequest):
    user: 'User'

class AppHttpRequestWithProject(AppHttpRequest):
    project: 'Project'