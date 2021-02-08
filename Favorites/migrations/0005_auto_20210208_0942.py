# Generated by Django 3.1.5 on 2021-02-08 09:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Colleges', '0001_initial'),
        ('Majors', '0008_auto_20210207_0950'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Favorites', '0004_auto_20210207_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoritemajors',
            options={'verbose_name': 'Favorite Major', 'verbose_name_plural': 'Favorite Majors'},
        ),
        migrations.AlterField(
            model_name='favoritecolleges',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 9, 42, 56, 229130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='favoritemajors',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 9, 42, 56, 229648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='favoritemajors',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majors_name', to='Majors.majors'),
        ),
        migrations.AlterField(
            model_name='favoritemajors',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_for_majors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='favoritecolleges',
            unique_together={('user', 'base')},
        ),
        migrations.AlterUniqueTogether(
            name='favoritemajors',
            unique_together={('user', 'base')},
        ),
    ]