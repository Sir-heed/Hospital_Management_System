# Generated by Django 3.0.7 on 2020-07-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20200702_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='bloodgroup',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], default='A', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='genotype',
            field=models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS')], default='AS', max_length=2),
            preserve_default=False,
        ),
    ]
