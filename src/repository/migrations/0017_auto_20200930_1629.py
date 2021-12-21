# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-30 16:29
from __future__ import unicode_literals

import core.file_system
from django.db import migrations, models
import repository.models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0016_auto_20200930_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preprint',
            name='meta_image',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=repository.models.preprint_file_upload),
        ),
        migrations.AlterField(
            model_name='repository',
            name='favicon',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=repository.models.repo_media_upload),
        ),
        migrations.AlterField(
            model_name='repository',
            name='hero_background',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=repository.models.repo_media_upload),
        ),
        migrations.AlterField(
            model_name='repository',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=repository.models.repo_media_upload),
        ),
    ]
