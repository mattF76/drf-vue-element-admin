# Generated by Django 4.2.7 on 2023-11-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userRole',
            field=models.ManyToManyField(blank=True, null=True, to='user.role'),
        ),
    ]
