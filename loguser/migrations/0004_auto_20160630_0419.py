# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loguser', '0003_auto_20160630_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Description',
            field=models.TextField(),
        ),
    ]
