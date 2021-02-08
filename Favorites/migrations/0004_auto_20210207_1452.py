# Generated by Django 3.1.5 on 2021-02-07 14:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Colleges', '0001_initial'),
        ('Favorites', '0003_auto_20210207_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecolleges',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 14, 52, 11, 499041, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='favoritecolleges',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colleges_name', to='Colleges.colleges'),
        ),
        migrations.AlterField(
            model_name='favoritemajors',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 7, 14, 52, 11, 499605, tzinfo=utc)),
        ),
    ]
