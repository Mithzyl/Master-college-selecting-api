# Generated by Django 3.1.5 on 2021-02-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Majors', '0006_auto_20210207_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majors',
            name='classes',
            field=models.CharField(choices=[('专业学位', '专业学位'), ('学术学位', '学术学位')], max_length=10),
        ),
    ]