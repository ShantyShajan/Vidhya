# Generated by Django 4.1.7 on 2023-04-24 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0055_meet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meet',
            name='link',
        ),
        migrations.RemoveField(
            model_name='video',
            name='link',
        ),
        migrations.RemoveField(
            model_name='video',
            name='time',
        ),
    ]
