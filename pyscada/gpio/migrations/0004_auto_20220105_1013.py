# Generated by Django 2.2.8 on 2022-01-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpio', '0003_auto_20200211_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpiodevice',
            name='board',
            field=models.CharField(choices=[('rpi', 'Raspberry Pi')], default='rpi', max_length=254),
        ),
    ]
