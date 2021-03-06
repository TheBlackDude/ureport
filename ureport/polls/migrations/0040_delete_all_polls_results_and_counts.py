# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from ureport.utils import chunk_list

# language=SQL;
CUSTOM_SQL = """
TRUNCATE polls_pollresult, polls_pollresultscounter;
"""


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0039_pollresult_ward'),
    ]

    operations = [
        migrations.RunSQL(CUSTOM_SQL)
    ]
