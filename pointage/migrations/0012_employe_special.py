# Generated by Django 5.0.6 on 2024-06-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointage', '0011_alter_history_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='special',
            field=models.SmallIntegerField(default=0),
        ),
    ]
