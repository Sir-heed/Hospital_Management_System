# Generated by Django 3.0.7 on 2020-07-02 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20200701_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalhistory',
            name='comment',
        ),
    ]
