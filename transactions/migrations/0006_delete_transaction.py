# Generated by Django 2.1.2 on 2018-10-25 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_transaction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
