# Generated by Django 3.1.5 on 2021-02-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstMajorSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ForeignLanguageSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PoliticSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SecondMajorSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
