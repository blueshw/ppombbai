# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppoombbai', '0003_auto_20151029_0636'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TEvent2',
        ),
        migrations.RemoveField(
            model_name='tevent',
            name='title2',
        ),
    ]
