# Generated by Django 2.0.2 on 2018-03-02 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_auto_20180302_1244'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='topiccategory',
            unique_together=set(),
        ),
    ]
