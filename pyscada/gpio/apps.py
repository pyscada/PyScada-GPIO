# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PyScadaGPIOConfig(AppConfig):
    name = 'pyscada.gpio'
    verbose_name = _("PyScada GPIO")
    path = os.path.dirname(os.path.realpath(__file__))
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        import pyscada.gpio.signals
