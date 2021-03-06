import os
import sys

from django.core.asgi import get_asgi_application


app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, '{{ cookiecutter.project_slug }}'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hejsvejs.settings')

application = get_asgi_application()
