# Generated by Django 4.2.2 on 2023-07-18 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("governanceplatform", "0009_remove_proxy_token_null"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": (
                    ("import_user", "Can import user"),
                    ("export_user", "Can export user"),
                )
            },
        ),
    ]