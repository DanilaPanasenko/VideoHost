# Generated by Django 5.1.1 on 2024-10-18 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='url',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
    ]
