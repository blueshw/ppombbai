# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TEvent',
            fields=[
                ('uid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('season_uid', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('from_user_uid', models.IntegerField()),
                ('to_user_uid', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('create_dt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 't_event',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TSeason',
            fields=[
                ('uid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=4)),
                ('start_dt', models.DateTimeField(auto_now=True)),
                ('end_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 't_season',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TSeasonResult',
            fields=[
                ('uid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('season_uid', models.IntegerField()),
                ('from_user_uid', models.IntegerField()),
                ('to_user_uid', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 't_season_result',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('uid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 't_user',
                'managed': True,
            },
        ),
    ]
