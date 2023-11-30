# Generated by Django 4.2 on 2023-11-29 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("incidents", "0008_remove_email_days_before_send_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sectorregulation",
            name="closing_email",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="closing_email",
                to="incidents.email",
            ),
        ),
        migrations.AddField(
            model_name="sectorregulation",
            name="opening_email",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="opening_email",
                to="incidents.email",
            ),
        ),
        migrations.AddField(
            model_name="email",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
