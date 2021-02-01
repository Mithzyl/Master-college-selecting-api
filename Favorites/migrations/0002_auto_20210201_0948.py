# Generated by Django 3.1.5 on 2021-02-01 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Colleges', '0001_initial'),
        ('Favorites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritemajors',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoritecolleges',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Colleges.colleges'),
        ),
        migrations.AddField(
            model_name='favoritecolleges',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]