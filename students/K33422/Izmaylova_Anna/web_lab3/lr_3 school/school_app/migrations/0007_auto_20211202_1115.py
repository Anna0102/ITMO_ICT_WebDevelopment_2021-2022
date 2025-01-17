# Generated by Django 3.2.8 on 2021-12-02 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0006_alter_teacher_group_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentsgroup',
            name='class_name',
        ),
        migrations.AddField(
            model_name='studentsgroup',
            name='class_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_app.groups'),
        ),
    ]
