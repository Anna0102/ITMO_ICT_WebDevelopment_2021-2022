# Generated by Django 3.2.8 on 2021-11-26 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='students_group_id',
        ),
    ]
