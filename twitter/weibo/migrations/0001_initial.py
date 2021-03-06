# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-12 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MOOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default=b'\xe4\xb8\x8d\xe6\x84\xbf\xe6\x84\x8f\xe9\x80\x8f\xe9\x9c\xb2\xe8\xba\xab\xe4\xbb\xbd\xe7\x9a\x84\xe4\xba\xba', max_length=10)),
                ('message', models.TextField()),
                ('dell_pass', models.CharField(max_length=10)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weibo.MOOD')),
            ],
        ),
    ]
