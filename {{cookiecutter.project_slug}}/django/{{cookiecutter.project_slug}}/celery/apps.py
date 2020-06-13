from django.apps import apps, AppConfig
from django.conf import settings

from .app import app

class CeleryAppConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.celery'
    verbose_name = 'Celery'

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)

        {% if cookiecutter.use_sentry == 'y' -%}
        if hasattr(settings, 'RAVEN_CONFIG'):
            # Celery signal registration
{% if cookiecutter.use_pycharm == 'y' -%}
	    # Since raven is required in production only,
            # imports might (most surely will) be wiped out
            # during PyCharm code clean up started
            # in other environments.
            # @formatter:off
{%- endif %}
            from raven import Client as RavenClient
            from raven.contrib.celery import register_signal as raven_register_signal
            from raven.contrib.celery import register_logger_signal as raven_register_logger_signal
{% if cookiecutter.use_pycharm == 'y' -%}
            # @formatter:on
{%- endif %}

            raven_client = RavenClient(dsn=settings.RAVEN_CONFIG['dsn'])
            raven_register_logger_signal(raven_client)
            raven_register_signal(raven_client)
        {%- endif %}
