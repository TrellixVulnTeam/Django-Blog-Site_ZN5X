# Generated by Django 2.1.2 on 2018-10-27 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20181027_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='share',
            name='persons',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Share',
        ),
    ]
