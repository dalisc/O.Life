# Generated by Django 2.2.5 on 2019-09-19 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190920_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user_account',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='user_account',
        ),
    ]