# Generated by Django 4.2.15 on 2024-08-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskdata',
            name='risk_a',
            field=models.FloatField(default=-1, verbose_name='Availability risk'),
        ),
        migrations.AddField(
            model_name='riskdata',
            name='risk_c',
            field=models.FloatField(default=-1, verbose_name='Confidentility risk'),
        ),
        migrations.AddField(
            model_name='riskdata',
            name='risk_i',
            field=models.FloatField(default=-1, verbose_name='Integrity risk'),
        ),
    ]
