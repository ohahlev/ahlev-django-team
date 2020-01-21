from django.apps import AppConfig
from . import __version__ as VERSION

class TeamConfig(AppConfig):
    name = "team"
    verbose_name = "Teammate Management %s" % VERSION
