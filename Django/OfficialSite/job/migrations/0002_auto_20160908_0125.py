# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='assortment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_assortment', to='job.Assortment', verbose_name='\u62db\u8058\u5206\u7c7b'),
        ),
    ]
