# Generated by Django 5.0.3 on 2024-06-19 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pointage', '0009_logs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='logs',
            new_name='History',
        ),
    ]