# Generated by Django 4.1.7 on 2023-03-31 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0044_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='uid',
            field=models.CharField(default='', max_length=50),
        ),
    ]
