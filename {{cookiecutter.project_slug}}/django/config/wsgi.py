import os
import sys

from django.core.wsgi import get_wsgi_application


app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, '{{ cookiecutter.project_slug }}'))
{% if cookiecutter.use_sentry == 'y' -%}
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
{%- endif %}
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_wsgi_application()
{% if cookiecutter.use_sentry == 'y' -%}
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.production':
    application = Sentry(application)
{%- endif %}
