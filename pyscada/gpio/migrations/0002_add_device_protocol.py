# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-24 12:49
from __future__ import unicode_literals
from pyscada.gpio import PROTOCOL_ID

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
    db_alias = schema_editor.connection.alias
    if not DeviceProtocol.objects.using(db_alias).filter(pk=PROTOCOL_ID):
        DeviceProtocol.objects.using(db_alias).bulk_create(
            [
                DeviceProtocol(
                    pk=PROTOCOL_ID,
                    protocol="gpio",
                    description="GPIO Interface",
                    app_name="pyscada.gpio",
                    device_class="pyscada.gpio.device",
                    daq_daemon=True,
                    single_thread=True,
                ),
            ]
        )


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
    db_alias = schema_editor.connection.alias
    DeviceProtocol.objects.using(db_alias).filter(protocol="gpio").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("gpio", "0001_initial"),
        ("pyscada", "0036_auto_20170224_1245"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
