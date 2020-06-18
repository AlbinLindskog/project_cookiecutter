"""
Basic error checking of the provided inputs, before we generate the project.
"""
import re

project_slug = "{{ cookiecutter.project_slug }}"

assert (
    re.match(r'[-._a-zA-Z][-._a-zA-Z0-9]*', project_slug)
), "'{}' project slug is invalid.".format(project_slug)