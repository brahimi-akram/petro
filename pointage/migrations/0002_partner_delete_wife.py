# Generated by Django 5.0.3 on 2024-05-20 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=30, null=True)),
                ('wilaya_of_birth', models.CharField(max_length=30, null=True)),
                ('marriage_date', models.DateField(null=True)),
                ('partner_salary', models.IntegerField(null=True)),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.employe')),
            ],
        ),
        migrations.DeleteModel(
            name='Wife',
        ),
    ]
