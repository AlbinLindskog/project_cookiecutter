"""
Clean up the files we ended up not using.
"""

import os
import shutil

REMOVE_PATHS = [
    {% if cookiecutter.use_react != 'y' %}'react',{% endif %}
    {% if cookiecutter.use_react != 'y' %}'docker/local/react',{% endif %}
    {% if cookiecutter.use_react != 'y' %}'compose/.envs/.local/.react',{% endif %}
    {% if cookiecutter.use_celery != 'y' %}'django/{{ cookiecutter.project_slug }}/celery',{% endif %}
    {% if cookiecutter.use_celery != 'y' %}'docker/local/celery',{% endif %}
    {% if cookiecutter.use_celery != 'y' %}'docker/production/celery',{% endif %}
    {% if cookiecutter.use_celery != 'y' %}'docker/production/beat',{% endif %}
    {% if cookiecutter.use_celery != 'y' %}'compose/.envs/redis',{% endif %}
    {% if cookiecutter.use_celery != 'y' %}'docker/local/redis',{% endif %}
    {% if cookiecutter.use_pycharm != 'y' %}'.idea',{% endif %}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)