# Generated by Django 3.0.7 on 2020-07-01 23:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='allergies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='diseases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='medications',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='surgeries',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='vaccinations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
    ]
