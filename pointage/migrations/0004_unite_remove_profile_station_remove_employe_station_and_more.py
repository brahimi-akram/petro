# Generated by Django 5.0.3 on 2024-06-01 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointage', '0003_alter_employe_driver_license_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unite_name', models.CharField(max_length=40, unique=True)),
                ('last_update', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='station',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='station',
        ),
        migrations.AlterField(
            model_name='employe',
            name='department',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='driver_license_type',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='enterprise',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='function',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='position',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='employe',
            name='service',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('validation', models.BooleanField(default=0)),
                ('active', models.BooleanField(default=0)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.employe')),
                ('unite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.unite')),
            ],
        ),
        migrations.AddField(
            model_name='employe',
            name='unite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pointage.unite'),
        ),
        migrations.AddField(
            model_name='profile',
            name='unite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pointage.unite'),
        ),
        migrations.DeleteModel(
            name='Station',
        ),
    ]
