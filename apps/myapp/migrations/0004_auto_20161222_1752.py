# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20161220_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='planner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tripplanner', to='myapp.User'),
        ),
        migrations.AlterUniqueTogether(
            name='trip',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
    ]
