from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from apps.accounts.forms import CreateOwnerAccount, CreateAccountFromInvite, Login
from apps.accounts.models import Role, User

@require_http_methods(['GET', 'POST'])
def setup(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = CreateOwnerAccount()
            pass
        case 'POST':
            form = CreateOwnerAccount(request.POST)
            if form.is_valid() and form.passwords_match():
                user = User(
                    full_name=form.full_name,
                    email=form.email,
                    password=form.password
                )

                user.roles.add(Role.superadmin_role())
                user.save()

    return render(request, 'accounts/setup.html.j2', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def join(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = CreateAccountFromInvite()
            pass
        case 'POST':
            form = CreateAccountFromInvite(request.POST)
            if form.is_valid() and form.passwords_match():
                user = User(
                    full_name=form.full_name,
                    # email=form.email,
                    password=form.password
                )

                user.save()

    return render(request, 'accounts/join.html.j2', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def login(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = Login()
            pass
        case 'POST':
            form = Login(request.POST)
            if form.is_valid() and form.passwords_match():
                pass
    return render(request, 'accounts/login.html.j2', {
        'form': form
    })