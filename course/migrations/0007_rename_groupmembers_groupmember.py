# Generated by Django 3.2.7 on 2021-09-19 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0006_auto_20210919_1238'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupMembers',
            new_name='GroupMember',
        ),
    ]
