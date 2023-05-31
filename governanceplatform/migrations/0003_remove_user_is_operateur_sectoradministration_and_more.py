# Generated by Django 4.2 on 2023-05-30 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('governanceplatform', '0002_services_servicestranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_operateur',
        ),
        migrations.CreateModel(
            name='SectorAdministration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sector_administrator', models.BooleanField(default=False)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='governanceplatform.sector')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='sectors',
        ),
        migrations.AddField(
            model_name='user',
            name='sectors',
            field=models.ManyToManyField(through='governanceplatform.SectorAdministration', to='governanceplatform.sector'),
        ),
    ]