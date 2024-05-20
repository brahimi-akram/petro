# Generated by Django 5.0.3 on 2024-05-20 05:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('ID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=30, null=True)),
                ('wilaya_of_birth', models.CharField(max_length=30)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adresse', models.CharField(max_length=50, null=True)),
                ('adresse_wilaya', models.CharField(max_length=30, null=True)),
                ('father_name', models.CharField(max_length=30, null=True)),
                ('mother_name', models.CharField(max_length=30, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('familiy_situation', models.CharField(max_length=30, null=True)),
                ('numbre_of_children', models.IntegerField(null=True)),
                ('blood_type', models.CharField(max_length=5, null=True)),
                ('cnas_number', models.IntegerField(null=True)),
                ('function', models.CharField(max_length=30, null=True)),
                ('position', models.CharField(max_length=30, null=True)),
                ('enterprise', models.CharField(max_length=30, null=True)),
                ('recruitment_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('department', models.CharField(max_length=30, null=True)),
                ('service', models.CharField(max_length=30, null=True)),
                ('contract_number', models.CharField(max_length=40, null=True)),
                ('contract_effective_date', models.DateField(null=True)),
                ('contract_validation_date', models.DateField(null=True)),
                ('contract_termination_date', models.DateField(null=True)),
                ('national_service_departure_date', models.DateField(null=True)),
                ('national_service_returne_date', models.DateField(null=True)),
                ('national_service_recall_departure_date', models.DateField(null=True)),
                ('national_service_recallt_return_date', models.DateField(null=True)),
                ('account_number', models.IntegerField(null=True)),
                ('account_key', models.IntegerField(null=True)),
                ('account_agency', models.CharField(max_length=40, null=True)),
                ('driver_license_number', models.IntegerField(null=True)),
                ('driver_license_established_date', models.DateField(null=True)),
                ('driver_license_experation_date', models.DateField(null=True)),
                ('driver_license_type', models.CharField(max_length=5, null=True)),
                ('cni_number', models.IntegerField(null=True)),
                ('cni_established_date', models.DateField(null=True)),
                ('cni_established_by', models.CharField(max_length=60, null=True)),
                ('recovery', models.IntegerField(default=0)),
                ('refund_total', models.IntegerField(default=0)),
                ('refund_by_month', models.IntegerField(default=0)),
                ('active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Station', models.CharField(max_length=40, unique=True)),
                ('last_update', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValidDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('date_of_validation', models.DateField()),
                ('month', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Diplome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishment', models.CharField(max_length=40)),
                ('entry_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('diplome_name', models.CharField(max_length=70)),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Code_Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('open_to_edit', models.BooleanField(default=False)),
                ('last_update', models.DateField(default=django.utils.timezone.now)),
                ('stored', models.BooleanField(default=False)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.code')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_emp', to='pointage.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=30, null=True)),
                ('student', models.BooleanField(null=True)),
                ('af', models.CharField(max_length=30, null=True)),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Month_stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=6)),
                ('absent', models.IntegerField(default=0)),
                ('travail', models.IntegerField(default=0)),
                ('mission', models.IntegerField(default=0)),
                ('conge', models.IntegerField(default=0)),
                ('rs', models.IntegerField(default=0)),
                ('eve_fam', models.IntegerField(default=0)),
                ('mld', models.IntegerField(default=0)),
                ('abs_autorise', models.IntegerField(default=0)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('da', models.IntegerField(default=3)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pointage.station')),
            ],
        ),
        migrations.AddField(
            model_name='employe',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pointage.station'),
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(max_length=30, null=True)),
                ('wilaya_of_birth', models.CharField(max_length=30, null=True)),
                ('marriage_date', models.DateField(null=True)),
                ('wife_salary', models.IntegerField(null=True)),
                ('id_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointage.employe')),
            ],
        ),
    ]
