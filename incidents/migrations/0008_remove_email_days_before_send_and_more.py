# Generated by Django 4.2 on 2023-11-22 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0007_alter_email_email_type_sectorregulationworkflowemail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='days_before_send',
        ),
        migrations.RemoveField(
            model_name='email',
            name='email_type',
        ),
    ]
