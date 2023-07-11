# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-19 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pyscada", "0042_auto_20180604_1240"),
    ]

    operations = [
        migrations.CreateModel(
            name="GPIODevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "board",
                    models.CharField(
                        choices=[("rpi", "Raspberry Pi")], default="rpi", max_length=254
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GPIOVariable",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gpio_mode",
                    models.CharField(
                        choices=[
                            (
                                "Polling",
                                (
                                    ("input", "Input"),
                                    ("input_pull_up", "Input Pull Up"),
                                    ("input_pull_down", "Input Pull Down"),
                                    ("output", "Output"),
                                ),
                            ),
                            (
                                "Interupt Rising Edge (not implemented)",
                                (
                                    ("input_pull_up_rising", "Input Pull Up"),
                                    ("input_pull_down_rising", "Input Pull Down"),
                                ),
                            ),
                            (
                                "Interupt Falling Edge (not implemented)",
                                (
                                    ("input_pull_up_falling", "Input Pull Up"),
                                    ("input_pull_down_falling", "Input Pull Down"),
                                ),
                            ),
                            (
                                "Interupt Both Edges (not implemented)",
                                (
                                    ("input_pull_up_both", "Input Pull Up"),
                                    ("input_pull_down_both", "Input Pull Down"),
                                ),
                            ),
                        ],
                        max_length=254,
                    ),
                ),
                (
                    "gpio_pin",
                    models.CharField(
                        help_text="pin number in Board notation (pin number of the pin header)",
                        max_length=254,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExtendedGPIODevice",
            fields=[],
            options={
                "verbose_name": "GPIO Device",
                "proxy": True,
                "verbose_name_plural": "GPIO Devices",
                "indexes": [],
            },
            bases=("pyscada.device",),
        ),
        migrations.CreateModel(
            name="ExtendedGPIOVariable",
            fields=[],
            options={
                "verbose_name": "GPIO Variable",
                "proxy": True,
                "verbose_name_plural": "GPIO Variables",
                "indexes": [],
            },
            bases=("pyscada.variable",),
        ),
        migrations.AddField(
            model_name="gpiovariable",
            name="gpio_variable",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pyscada.Variable",
            ),
        ),
        migrations.AddField(
            model_name="gpiodevice",
            name="gpio_device",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pyscada.Device",
            ),
        ),
    ]
