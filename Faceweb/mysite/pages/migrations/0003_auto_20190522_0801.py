# Generated by Django 2.2.1 on 2019-05-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentaffairs',
            name='is_studentaffairs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
