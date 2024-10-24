# Generated by Django 5.1.2 on 2024-10-18 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("incidents", "0023_remove_answer_predefined_answer_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="questioncategoryoptions",
            options={
                "verbose_name": "Question category option",
                "verbose_name_plural": "Question category options",
            },
        ),
        migrations.AddField(
            model_name="questioncategoryoptions",
            name="report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="incidents.workflow",
            ),
        ),
        migrations.AddField(
            model_name="questionoptions",
            name="category_option",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="incidents.questioncategoryoptions",
            ),
        ),
    ]
