# Generated by Django 4.0.1 on 2022-01-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hometask', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submissionmodel',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='hometaskmodel',
            name='penalty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='submissionmodel',
            name='grade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='submissionmodel',
            unique_together={('hometask', 'user', 'grade')},
        ),
    ]