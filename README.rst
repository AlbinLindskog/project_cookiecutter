Project Cookiecutter
====================
Quickly set up a modern, production ready web-project using cookiecutter: https://github.com/audreyr/cookiecutter

Features
---------
* For Django 3.0 with Python 3.6
* Backed by PostgreSQL 11.3
* Optionally includes React 16.13 for frontend
* Optionally includes celery 4.2 for asynchronous tasks
* Caddy 0.11 as reverse proxy and static/media file server
* Secure by default (SSL) with LetsEncrypts
* Live reloading in local development of both Django and React
* All services are Dockerized
* Docker-compose for development and single-server production setups
* Kubernetes for multiple-server production setup
* Optimized development and production settings
* Instructions for getting up and running, both in dev and production.
* Sentry for error reporting and Graylog for application logs.

Usage
------
Let's imagine you want to create a web-project call 'Moustache'. First, install Cookiecutter::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/AlbinLindskog/project-cookiecutter

You'll be prompted for some values. Provide them, and the project will be setup for you::

    Cloning into 'project-cookiecutter'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Cookiecutter project]: moustache
    project_slug [cookiecutter_project]: moustache
    domain_name [pinestreet.tech]: moustache.com
    email [albin@pinestreet.tech]: albin@moustache.com
    version [0.0.1]:
    use_pycharm [y]: y
    use_react [y]: y
    use_celery [y]: y
    use_sentry [y]: y
    use_graylog [y]: y
    debug [n]: y

Enter the project and take a look around::

    $ cd moustache/
    $ ls

Create a git repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "Mustasche project stated with cookiecutter"
    $ git remote add origin git@github.com:AlbinLindskog/mustasche.git
    $ git push -u origin master

Now take a look at the README in your repo. It contains the instruction you need to get up and running both i dev and production.