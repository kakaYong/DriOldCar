# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='avideo name')),
                ('media_file', models.FileField(upload_to='')),
                ('actor_name', models.CharField(max_length=100, verbose_name='actor name')),
                ('country', models.CharField(choices=[('JAP', 'Janpen'), ('Chi', 'Chinese'), ('Kor', 'Korea'), ('USA', 'Unite states')], max_length=100, verbose_name='countryname')),
            ],
        ),
        migrations.CreateModel(
            name='LiveVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]