# Generated by Django 2.1.4 on 2019-01-17 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('kuotes', '0006_kuote_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kuote',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
