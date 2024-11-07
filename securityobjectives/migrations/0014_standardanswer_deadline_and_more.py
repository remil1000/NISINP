# Generated by Django 5.1.2 on 2024-11-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("securityobjectives", "0013_remove_securitymeasureanswer_sectors_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="standardanswer",
            name="deadline",
            field=models.DateTimeField(
                blank=True, default=None, null=True, verbose_name="Deadline"
            ),
        ),
        migrations.AddField(
            model_name="standardanswer",
            name="review_comment",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Review comment"
            ),
        ),
    ]
