# Generated by Django 4.2.7 on 2023-11-29 10:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("incidents", "0009_alter_incident_incident_detection_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incident",
            name="incident_detection_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="incident",
            name="incident_notification_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="incident",
            name="incident_starting_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]