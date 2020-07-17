# Generated by Django 3.0.7 on 2020-07-16 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergy',
            old_name='name',
            new_name='allergy_name',
        ),
        migrations.RenameField(
            model_name='disease',
            old_name='name',
            new_name='disease_name',
        ),
        migrations.RenameField(
            model_name='medication',
            old_name='name',
            new_name='medication_name',
        ),
        migrations.RenameField(
            model_name='surgery',
            old_name='name',
            new_name='surgery_name',
        ),
        migrations.RenameField(
            model_name='vaccination',
            old_name='name',
            new_name='vaccination_name',
        ),
    ]
