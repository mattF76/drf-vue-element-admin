# Generated by Django 4.2.7 on 2023-11-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_account_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='账号名'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='permissionName',
            field=models.CharField(max_length=200, unique=True, verbose_name='权限名'),
        ),
        migrations.AlterField(
            model_name='role',
            name='roleName',
            field=models.CharField(max_length=20, unique=True, verbose_name='角色名'),
        ),
    ]