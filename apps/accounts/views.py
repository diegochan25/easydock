from datetime import timedelta

from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods
from apps.accounts.forms import CreateOwnerAccount, CreateAccountFromInvite, SignIn, ForgotPassword, ResetPassword
from apps.accounts.models import User

@require_http_methods(['GET', 'POST'])
def setup(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = CreateOwnerAccount()
        case 'POST':
            form = CreateOwnerAccount(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if User.objects.filter(email=data['email']).exists():
                    messages.error(request, 'A user with this email already exists.')
                    return render(request, 'accounts/setup.html.j2', { 'form': form })
                User.objects.create_superuser(
                    email=data['email'],
                    password=data['password'],
                    full_name=data['full_name'],
                )
                messages.success(request, 'The owner account was created successfully.')
                return redirect('accounts:sign_in')

    return render(request, 'accounts/setup.html.j2', { 'form': form })

@require_http_methods(['GET', 'POST'])
def join(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = CreateAccountFromInvite()
        case 'POST':
            form = CreateAccountFromInvite(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                User.objects.create_superuser(
                    # email=data['email'],
                    password=data['password'],
                    full_name=data['full_name'],
                )
                messages.success(request, 'Your account was created successfully.')
                return redirect('accounts:sign_in')

    return render(request, 'accounts/join.html.j2', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def sign_in(request: HttpRequest):
    default_intent = 'projects:index'

    if request.user.is_authenticated:
        return redirect(default_intent)
    
    match (request.method):
        case 'GET':
            form = SignIn()
        case 'POST':
            form = SignIn(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(request, username=data['email'], password=data['password'])
                if user is None:
                    messages.error(request, 'Please check your credentials and try again')
                else: 
                    login(request, user)
                    ttl = timedelta(days=30) if data['remember_me'] else timedelta(hours=8)
                    request.session.set_expiry(ttl)

                intent = request.GET.get('next', default_intent)
                if not url_has_allowed_host_and_scheme(intent, allowed_hosts={request.get_host()}):
                    intent = default_intent
                return redirect(intent)

    return render(request, 'accounts/sign-in.html.j2', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def forgot_password(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = ForgotPassword()
        case 'POST':
            form = ForgotPassword(request.POST)
            if form.is_valid():
                data = form.cleaned_data
    return render(request, 'accounts/forgot-password.html.j2', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def reset_password(request: HttpRequest):
    match (request.method):
        case 'GET':
            form = ResetPassword()
        case 'POST':
            form = ResetPassword(request.POST)
            if form.is_valid():
                data = form.cleaned_data
    return render(request, 'accounts/reset-password.html.j2', {
        'form': form
    })