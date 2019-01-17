# Generated by Django 2.1.4 on 2019-01-15 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuotes', '0004_twitteraccount_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='avatar_url',
            field=models.URLField(blank=True, verbose_name='Avatar URL'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]