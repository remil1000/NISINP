# Generated by Django 4.2 on 2024-02-07 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('governanceplatform', '0008_sectorcompanycontact_remove_sectorcontact_sector_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyuser',
            name='company',
        ),
        migrations.RemoveField(
            model_name='companyuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='SectorContact',
        ),
        migrations.DeleteModel(
            name='CompanyUser',
        ),
    ]
