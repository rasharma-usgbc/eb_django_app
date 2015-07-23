#!/tmp/eb_django_app/bin/python2.7
from django.core import management

if __name__ == "__main__":
    management.execute_from_command_line()

export DJANGO_SETTINGS_MODULE=mysite.settings
django-admin.py runserver
