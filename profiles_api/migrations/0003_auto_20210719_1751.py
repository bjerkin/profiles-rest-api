# Generated by Django 2.2 on 2021-07-19 17:51

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20210719_1751'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
