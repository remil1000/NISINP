# Generated by Django 5.1 on 2024-08-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reporting", "0003_alter_recommendationdata_due_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicestat",
            name="high_risk_average",
        ),
        migrations.RemoveField(
            model_name="servicestat",
            name="high_risk_rate",
        ),
        migrations.RemoveField(
            model_name="servicestat",
            name="threshold_for_high_risk",
        ),
        migrations.AddField(
            model_name="servicestat",
            name="avg_current_risks",
            field=models.FloatField(default=0, verbose_name="Average of current risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="avg_residual_risks",
            field=models.FloatField(
                default=0, verbose_name="Average of residual risks"
            ),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_accepted_risks",
            field=models.FloatField(default=0, verbose_name="Total of accepted risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_denied_risks",
            field=models.FloatField(default=0, verbose_name="Total of denied risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_reduced_risks",
            field=models.FloatField(default=0, verbose_name="Total of reduced risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_risks",
            field=models.FloatField(default=0, verbose_name="Total of all risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_shared_risks",
            field=models.FloatField(default=0, verbose_name="Total of shared risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_treated_risks",
            field=models.FloatField(default=0, verbose_name="Total of treated risks"),
        ),
        migrations.AddField(
            model_name="servicestat",
            name="total_untreated_risks",
            field=models.FloatField(default=0, verbose_name="Total of untreated risks"),
        ),
    ]
