# Generated by Django 2.2.3 on 2020-09-13 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zdrowadieta', '0011_auto_20200913_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
    ]
