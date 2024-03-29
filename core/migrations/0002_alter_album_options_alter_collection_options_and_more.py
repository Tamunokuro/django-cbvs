# Generated by Django 4.1 on 2022-08-22 12:58

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='album',
            name='created',
            field=models.TimeField(auto_now_add=True, default=datetime.datetime(2022, 8, 22, 12, 57, 51, 75365, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='created',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
