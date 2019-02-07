# Generated by Django 2.1.4 on 2019-02-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('kuotes', '0009_kuote_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kuote',
            name='title',
        ),
        migrations.AddField(
            model_name='source',
            name='title',
            field=models.CharField(default='blank title', max_length=280),
            preserve_default=False,
        ),
    ]