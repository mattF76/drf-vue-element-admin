# Generated by Django 4.2.7 on 2023-12-05 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_account_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='rolePermission',
            new_name='rolePermissions',
        ),
    ]
