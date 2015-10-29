# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppoombbai', '0002_remove_tevent_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEvent2',
            fields=[
                ('uid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('season_uid', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('title2', models.CharField(max_length=255)),
                ('from_user_uid', models.IntegerField()),
                ('receive_user_uid', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('create_dt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'managed': True,
                'db_table': 't_event2',
            },
        ),
        migrations.RenameField(
            model_name='tevent',
            old_name='to_user_uid',
            new_name='receive_user_uid',
        ),
        migrations.AddField(
            model_name='tevent',
            name='title',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tevent',
            name='title2',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
