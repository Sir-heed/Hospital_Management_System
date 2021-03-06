# Generated by Django 3.0.7 on 2020-07-16 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('bloodgroup', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('genotype', models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS')], max_length=2)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('medicalHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccination', to='record.MedicalHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('medicalHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgery', to='record.MedicalHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('medicalHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication', to='record.MedicalHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('medicalHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disease', to='record.MedicalHistory')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('medicalHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergy', to='record.MedicalHistory')),
            ],
        ),
    ]
