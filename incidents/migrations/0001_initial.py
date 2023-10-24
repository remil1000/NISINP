# Generated by Django 4.2 on 2023-10-24 07:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('governanceplatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_type', models.CharField(choices=[('PRELI', 'Preliminary notification'), ('FINAL', 'Final notification'), ('ADD', 'Additional notification'), ('REMIND', 'Reminder : final notification not done')], default='PRELI', max_length=10)),
                ('days_before_send', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_generic_impact', models.BooleanField(default=False, verbose_name='Generic Impact')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PredefinedAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('FREETEXT', 'Freetext'), ('MULTI', 'Multiple Choice'), ('SO', 'Single Option Choice'), ('MT', 'Multiple Choice + Free Text'), ('ST', 'Single Choice + Free Text'), ('CL', 'Country list'), ('RL', 'Region list'), ('DATE', 'Date picker')], default='FREETEXT', max_length=10)),
                ('is_mandatory', models.BooleanField(default=False, verbose_name='Mandatory')),
                ('is_preliminary', models.BooleanField(default=False, verbose_name='Preliminary')),
                ('position', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Question Category',
                'verbose_name_plural': 'Question Categories',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Reglementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impacts', models.ManyToManyField(blank=True, default=None, to='incidents.impact')),
                ('regulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceplatform.regulation')),
                ('regulator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceplatform.regulator')),
                ('sectors', models.ManyToManyField(blank=True, default=None, to='governanceplatform.sector')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='incidents.question')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReglementationWorkflows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, default=0, null=True)),
                ('reglementation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidents.reglementation')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidents.workflow')),
            ],
        ),
        migrations.AddField(
            model_name='reglementation',
            name='workflows',
            field=models.ManyToManyField(through='incidents.ReglementationWorkflows', to='incidents.workflow'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='incidents.questioncategory'),
        ),
        migrations.AddField(
            model_name='question',
            name='predefined_answers',
            field=models.ManyToManyField(blank=True, to='incidents.predefinedanswer'),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.CharField(max_length=22, verbose_name='Incident identifier')),
                ('incident_notification_date', models.DateField(default=datetime.date.today)),
                ('company_name', models.CharField(max_length=100, verbose_name='Company name')),
                ('contact_lastname', models.CharField(max_length=100, verbose_name='contact lastname')),
                ('contact_firstname', models.CharField(max_length=100, verbose_name='contact firstname')),
                ('contact_title', models.CharField(max_length=100, verbose_name='contact title')),
                ('contact_email', models.CharField(max_length=100, verbose_name='contact email')),
                ('contact_telephone', models.CharField(max_length=100, verbose_name='contact telephone')),
                ('technical_lastname', models.CharField(max_length=100, verbose_name='technical lastname')),
                ('technical_firstname', models.CharField(max_length=100, verbose_name='technical firstname')),
                ('technical_title', models.CharField(max_length=100, verbose_name='technical title')),
                ('technical_email', models.CharField(max_length=100, verbose_name='technical email')),
                ('technical_telephone', models.CharField(max_length=100, verbose_name='technical telephone')),
                ('incident_reference', models.CharField(max_length=255)),
                ('complaint_reference', models.CharField(max_length=255)),
                ('is_significative_impact', models.BooleanField(default=False, verbose_name='Significative impact')),
                ('review_status', models.CharField(choices=[('DELIV', 'Delivered but not yet reviewed'), ('PASS', 'Review passed'), ('FAIL', 'Review failed'), ('OUT', 'Final notification missing. due date exceeded')], default='DELIV', max_length=5)),
                ('incident_status', models.CharField(choices=[('CLOSE', 'Closed'), ('GOING', 'On-going')], default='CLOSE', max_length=5)),
                ('Reglementation', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='incidents.reglementation')),
                ('affected_services', models.ManyToManyField(to='governanceplatform.service')),
                ('authorities', models.ManyToManyField(related_name='authorities', to='governanceplatform.regulator')),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='governanceplatform.company')),
                ('contact_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('impacts', models.ManyToManyField(default=None, to='incidents.impact')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidents.incident')),
                ('predefined_answers', models.ManyToManyField(blank=True, to='incidents.predefinedanswer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidents.question')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.workflow')),
            ],
            options={
                'verbose_name': 'workflow Translation',
                'db_table': 'incidents_workflow_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReglementationTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.reglementation')),
            ],
            options={
                'verbose_name': 'reglementation Translation',
                'db_table': 'incidents_reglementation_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.TextField()),
                ('tooltip', models.TextField(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.question')),
            ],
            options={
                'verbose_name': 'question Translation',
                'db_table': 'incidents_question_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestionCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.questioncategory')),
            ],
            options={
                'verbose_name': 'Question Category Translation',
                'db_table': 'incidents_questioncategory_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PredefinedAnswerTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('predefined_answer', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.predefinedanswer')),
            ],
            options={
                'verbose_name': 'predefined answer Translation',
                'db_table': 'incidents_predefinedanswer_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ImpactTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.impact')),
            ],
            options={
                'verbose_name': 'impact Translation',
                'db_table': 'incidents_impact_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EmailTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('subject', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('content', models.TextField()),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='incidents.email')),
            ],
            options={
                'verbose_name': 'email Translation',
                'db_table': 'incidents_email_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
