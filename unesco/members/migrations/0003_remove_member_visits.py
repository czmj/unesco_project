# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_visits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='visits',
        ),
    ]
