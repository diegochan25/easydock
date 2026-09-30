# EasyDock

A web app for managing Docker networks and containers as services, in a PaaS-like environment. Instead of juggling `docker run` flags and compose files, you describe projects and their services in the UI and let EasyDock handle the containers and networks behind them.

> **Status:** early development. The project scaffold, tooling and frontend pipeline are in place; the Docker management features are still to be built.

## Concepts

- **Project** – a group of related services that share an isolated Docker network.
- **Service** – a container managed as a deployable unit (image, environment, ports, volumes, lifecycle).
- **Network** – Docker networks that connect services within a project.

## Stack

- [Django](https://www.djangoproject.com/) 6 with [Jinja2](https://jinja.palletsprojects.com/) templates (the Django engine is kept for the admin)
- [Tailwind CSS](https://tailwindcss.com/) v4 via [django-tailwind](https://github.com/timonweb/django-tailwind), using the standalone binary (no Node.js needed)
- [WhiteNoise](https://whitenoise.readthedocs.io/) for static files
- [django-environ](https://django-environ.readthedocs.io/) for configuration
- [django-browser-reload](https://github.com/adamchainz/django-browser-reload) for auto-reload in development
- SQLite for the database
- [uv](https://docs.astral.sh/uv/) for dependency management (Python 3.14+)

## Project layout

```
config/            Django project: settings (base/development/production), urls, Jinja2 environment
apps/accounts/     Users and authentication
apps/projects/     Projects, services and networks
apps/theme/        Tailwind app (CSS source in static_src/, base template)
templates/         Project-wide Jinja2 templates (layouts, macros, partials)
static/            Project-wide static files
```

Jinja2 templates live in `templates/` folders, both at the project root and inside each app (`apps/<app>/templates/`). Jinja2 is tried first; templates it can't find, such as the admin's, fall back to the Django engine.

## Getting started

Requirements: Python 3.14+ and [uv](https://docs.astral.sh/uv/).

```sh
# 1. Install dependencies
uv sync

# 2. Configure the environment
cp .env.example .env.dev
#    then edit .env.dev and set a SECRET_KEY

# 3. Set up the database
uv run python manage.py migrate
uv run python manage.py createsuperuser   # optional

# 4. Run the dev server and the Tailwind watcher (in two terminals)
uv run python manage.py runserver
uv run python manage.py tailwind dev
```

The Tailwind standalone binary is downloaded automatically on first use. With `django-browser-reload` enabled, the page refreshes when templates, Python files or the built CSS change.

## Configuration

Settings are read from an env file. By default `.env.dev` is loaded; set `ENV_FILE` to use another one.

| Variable        | Description                                             |
| --------------- | ------------------------------------------------------- |
| `SECRET_KEY`    | Django secret key (required)                            |
| `PYTHON_ENV`    | `development` enables `DEBUG`; anything else disables it |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames               |

Settings modules: `config.settings.development` (default in `manage.py`) and `config.settings.production`. Select one with `DJANGO_SETTINGS_MODULE`.

## Production build

```sh
uv run python manage.py tailwind build
uv run python manage.py collectstatic --noinput
```

Run with `DJANGO_SETTINGS_MODULE=config.settings.production` and a WSGI/ASGI server (`config.wsgi` / `config.asgi`). WhiteNoise serves the collected static files.

## Tailwind

Styles are written in [apps/theme/static_src/src/styles.css](apps/theme/static_src/src/styles.css). The build output (`apps/theme/static/css/dist/styles.css`) is git-ignored. In Jinja2 templates, include it with `{{ tailwind_css() }}`; the base template is [apps/theme/templates/base.html](apps/theme/templates/base.html).
