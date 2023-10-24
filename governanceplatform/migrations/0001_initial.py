# Generated by Django 4.2 on 2023-10-24 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields
import parler.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(error_messages={'unique': 'A user is already registered with this email address'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=30, null=True, region=None)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Administrator')),
            ],
            options={
                'permissions': (('import_user', 'Can import user'), ('export_user', 'Can export user')),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_regulator', models.BooleanField(default=False, verbose_name='Regulator')),
                ('identifier', models.CharField(max_length=4, verbose_name='Identifier')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('country', models.CharField(max_length=64, verbose_name='country')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('email', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='email address')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=30, null=True, region=None)),
                ('monarc_path', models.CharField(max_length=200, verbose_name='MONARC URL')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyAdministrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_company_administrator', models.BooleanField(default=False, verbose_name='Administrator')),
            ],
            options={
                'verbose_name': 'Company administrator',
                'verbose_name_plural': 'Company administrator',
            },
        ),
        migrations.CreateModel(
            name='Functionality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Functionality',
                'verbose_name_plural': 'Functionalities',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FunctionalityTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Functionality Translation',
                'db_table': 'governanceplatform_functionality_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OperatorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OperatorTypeTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'operator type Translation',
                'db_table': 'governanceplatform_operatortype_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RegulationTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'regulation Translation',
                'db_table': 'governanceplatform_regulation_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Regulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('country', models.CharField(max_length=64, verbose_name='country')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('monarc_path', models.CharField(max_length=200, verbose_name='MONARC URL')),
                ('email_for_notification', models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='email address')),
                ('full_name', models.TextField(blank=True, default='', null=True, verbose_name='full name')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='description')),
                ('is_receiving_all_incident', models.BooleanField(default=False, verbose_name='Receive all incident')),
            ],
            options={
                'verbose_name': 'Regulator',
                'verbose_name_plural': 'Regulators',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='governanceplatform.sector', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectors',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceplatform.sector')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServiceTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='governanceplatform.service')),
            ],
            options={
                'verbose_name': 'Service Translation',
                'db_table': 'governanceplatform_service_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SectorTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='governanceplatform.sector')),
            ],
            options={
                'verbose_name': 'Sector Translation',
                'db_table': 'governanceplatform_sector_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SectorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sector_contact', models.BooleanField(default=False, verbose_name='Contact person')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceplatform.sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sector contact',
                'verbose_name_plural': 'Sectors contact',
            },
        ),
    ]
