# Generated by Django 5.0.3 on 2024-06-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointage', '0010_rename_logs_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
