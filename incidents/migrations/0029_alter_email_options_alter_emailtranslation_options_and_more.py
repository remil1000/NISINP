# Generated by Django 5.1.2 on 2024-12-10 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "governanceplatform",
            "0038_alter_company_options_alter_regulator_options_and_more",
        ),
        ("incidents", "0028_alter_questionoptions_category_option"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="email",
            options={"verbose_name": "Email", "verbose_name_plural": "Emails"},
        ),
        migrations.AlterModelOptions(
            name="emailtranslation",
            options={
                "default_permissions": (),
                "managed": True,
                "verbose_name": "Email Translation",
            },
        ),
        migrations.AlterModelOptions(
            name="questioncategory",
            options={
                "verbose_name": "Step in notification form",
                "verbose_name_plural": "Steps in notification form",
            },
        ),
        migrations.AlterModelOptions(
            name="questioncategorytranslation",
            options={
                "default_permissions": (),
                "managed": True,
                "verbose_name": "Step in notification form Translation",
            },
        ),
        migrations.AlterModelOptions(
            name="sectorregulationworkflow",
            options={"verbose_name": "Reports", "verbose_name_plural": "Report"},
        ),
        migrations.AlterModelOptions(
            name="sectorregulationworkflowemail",
            options={
                "verbose_name": "Reminder email",
                "verbose_name_plural": "Reminder emails",
            },
        ),
        migrations.AlterModelOptions(
            name="sectorregulationworkflowemailtranslation",
            options={
                "default_permissions": (),
                "managed": True,
                "verbose_name": "Reminder email Translation",
            },
        ),
        migrations.AlterField(
            model_name="answer",
            name="incident_workflow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.incidentworkflow",
                verbose_name="Incident report processed",
            ),
        ),
        migrations.AlterField(
            model_name="impact",
            name="regulation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="governanceplatform.regulation",
                verbose_name="Legal basis",
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="affected_sectors",
            field=models.ManyToManyField(
                to="governanceplatform.sector", verbose_name="Impacted sectors"
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="affected_services",
            field=models.ManyToManyField(
                to="governanceplatform.service", verbose_name="Impacted service"
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="authorities",
            field=models.ManyToManyField(
                related_name="authorities",
                to="governanceplatform.regulator",
                verbose_name="Regulators",
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="company",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="governanceplatform.company",
                verbose_name="Operator",
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="company_name",
            field=models.CharField(max_length=100, verbose_name="Name of the Operator"),
        ),
        migrations.AlterField(
            model_name="incident",
            name="complaint_reference",
            field=models.CharField(
                max_length=255, verbose_name="Criminal complaint file number"
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="contact_email",
            field=models.CharField(max_length=100, verbose_name="Contact email"),
        ),
        migrations.AlterField(
            model_name="incident",
            name="contact_title",
            field=models.CharField(max_length=100, verbose_name="Contact job title"),
        ),
        migrations.AlterField(
            model_name="incident",
            name="incident_id",
            field=models.CharField(max_length=22, verbose_name="Incident ID"),
        ),
        migrations.AlterField(
            model_name="incident",
            name="incident_reference",
            field=models.CharField(
                max_length=255, verbose_name="Internal incident reference"
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="incident_status",
            field=models.CharField(
                choices=[("CLOSE", "Closed"), ("GOING", "Ongoing")],
                default="GOING",
                max_length=5,
                verbose_name="Incident status",
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="review_status",
            field=models.CharField(
                choices=[
                    ("UNDE", "Unsubmitted"),
                    ("DELIV", "Under review"),
                    ("PASS", "Passed"),
                    ("FAIL", "Failed"),
                    ("OUT", "Submission overdue"),
                ],
                default="UNDE",
                max_length=5,
                verbose_name="Report status",
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="technical_email",
            field=models.CharField(max_length=100, verbose_name="Technical email"),
        ),
        migrations.AlterField(
            model_name="incident",
            name="technical_title",
            field=models.CharField(max_length=100, verbose_name="Technical job title"),
        ),
        migrations.AlterField(
            model_name="incidentworkflow",
            name="review_status",
            field=models.CharField(
                choices=[
                    ("UNDE", "Unsubmitted"),
                    ("DELIV", "Under review"),
                    ("PASS", "Passed"),
                    ("FAIL", "Failed"),
                    ("OUT", "Submission overdue"),
                ],
                default="UNDE",
                max_length=5,
                verbose_name="Report status",
            ),
        ),
        migrations.AlterField(
            model_name="logreportread",
            name="incident",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.incident",
                verbose_name="Incident report processed",
            ),
        ),
        migrations.AlterField(
            model_name="logreportread",
            name="incident_report",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.incidentworkflow",
                verbose_name="Incident report processed",
            ),
        ),
        migrations.AlterField(
            model_name="logreportread",
            name="user_full_name",
            field=models.CharField(max_length=250, verbose_name="Full username"),
        ),
        migrations.AlterField(
            model_name="sectorregulation",
            name="closing_email",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="closing_email",
                to="incidents.email",
                verbose_name="Closing email",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulation",
            name="is_detection_date_needed",
            field=models.BooleanField(
                default=False, verbose_name="Incident detection date required"
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulation",
            name="opening_email",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="opening_email",
                to="incidents.email",
                verbose_name="Opening email",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulation",
            name="regulation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="governanceplatform.regulation",
                verbose_name="Legal basis",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulation",
            name="report_status_changed_email",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="report_status_changed_email",
                to="incidents.email",
                verbose_name="Status update email",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflow",
            name="delay_in_hours_before_deadline",
            field=models.IntegerField(default=0, verbose_name="Deadline in hours"),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflow",
            name="emails",
            field=models.ManyToManyField(
                through="incidents.SectorRegulationWorkflowEmail",
                to="incidents.email",
                verbose_name="Emails",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflow",
            name="trigger_event_before_deadline",
            field=models.CharField(
                choices=[
                    ("NONE", "None"),
                    ("NOTIF_DATE", "Notification Date"),
                    ("DETECT_DATE", "Detection Date"),
                    ("PREV_WORK", "Previous Workflow"),
                ],
                default="NONE",
                max_length=15,
                verbose_name="Event triggering deadline",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflowemail",
            name="delay_in_hours",
            field=models.IntegerField(default=0, verbose_name="Delay in hours"),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflowemail",
            name="email",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.email",
                verbose_name="Email",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflowemail",
            name="sector_regulation_workflow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.sectorregulationworkflow",
                verbose_name="Report",
            ),
        ),
        migrations.AlterField(
            model_name="sectorregulationworkflowemailtranslation",
            name="headline",
            field=models.CharField(max_length=255, verbose_name="Email subject"),
        ),
        migrations.AlterField(
            model_name="workflow",
            name="is_impact_needed",
            field=models.BooleanField(
                default=False, verbose_name="Impacts disclosure required"
            ),
        ),
        migrations.AlterField(
            model_name="workflow",
            name="submission_email",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="submission_email",
                to="incidents.email",
                verbose_name="Submision email",
            ),
        ),
    ]