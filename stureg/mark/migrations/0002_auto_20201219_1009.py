# Generated by Django 2.2.17 on 2020-12-19 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '__first__'),
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentMarkDetails',
            new_name='StudentMark',
        ),
    ]
