from .base import *  # noqa: F403

DEBUG = True

INSTALLED_APPS += ['django_browser_reload']  # noqa: F405

MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']  # noqa: F405

# Manifest storage requires collectstatic; use plain storage in development.
STORAGES['staticfiles'] = {  # noqa: F405
    'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
}
