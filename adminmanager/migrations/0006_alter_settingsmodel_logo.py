# Generated by Django 3.2.20 on 2023-09-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmanager', '0005_alter_settingsmodel_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsmodel',
            name='logo',
            field=models.ImageField(upload_to='sitelogo/'),
        ),
    ]
