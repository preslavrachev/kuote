# Generated by Django 2.1.4 on 2019-02-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('kuotes', '0008_auto_20190117_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='kuote',
            name='title',
            field=models.CharField(default='blank_title', max_length=280),
            preserve_default=False,
        ),
    ]
