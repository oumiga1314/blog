# Generated by Django 2.0.2 on 2018-03-03 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0014_auto_20180303_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topicvote',
            old_name='like',
            new_name='vote',
        ),
    ]
