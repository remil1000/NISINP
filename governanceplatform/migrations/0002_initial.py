# Generated by Django 4.2.5 on 2023-09-27 12:43

import django.db.models.deletion
import parler.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("governanceplatform", "0001_initial"),
        ("incidents", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sector",
            name="specific_impact",
            field=models.ManyToManyField(
                blank=True, default=None, to="incidents.impact"
            ),
        ),
        migrations.AddField(
            model_name="operatortypetranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="governanceplatform.operatortype",
            ),
        ),
        migrations.AddField(
            model_name="operatortype",
            name="functionalities",
            field=models.ManyToManyField(to="governanceplatform.functionality"),
        ),
        migrations.AddField(
            model_name="functionalitytranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="governanceplatform.functionality",
            ),
        ),
        migrations.AddField(
            model_name="companyadministrator",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="governanceplatform.company",
            ),
        ),
        migrations.AddField(
            model_name="companyadministrator",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="company",
            name="sectors",
            field=models.ManyToManyField(to="governanceplatform.sector"),
        ),
        migrations.AddField(
            model_name="company",
            name="types",
            field=models.ManyToManyField(to="governanceplatform.operatortype"),
        ),
        migrations.AddField(
            model_name="user",
            name="companies",
            field=models.ManyToManyField(
                through="governanceplatform.CompanyAdministrator",
                to="governanceplatform.company",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="sectors",
            field=models.ManyToManyField(
                through="governanceplatform.SectorContact",
                to="governanceplatform.sector",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="servicetranslation",
            unique_together={("language_code", "master")},
        ),
        migrations.AlterUniqueTogether(
            name="sectortranslation",
            unique_together={("language_code", "master")},
        ),
        migrations.AddConstraint(
            model_name="sectorcontact",
            constraint=models.UniqueConstraint(
                fields=("user", "sector"), name="unique_SectorContact"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="operatortypetranslation",
            unique_together={("language_code", "master")},
        ),
        migrations.AlterUniqueTogether(
            name="functionalitytranslation",
            unique_together={("language_code", "master")},
        ),
        migrations.AddConstraint(
            model_name="companyadministrator",
            constraint=models.UniqueConstraint(
                fields=("user", "company"), name="unique_CompanyAdministrator"
            ),
        ),
    ]
