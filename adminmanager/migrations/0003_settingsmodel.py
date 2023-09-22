# Generated by Django 3.2.20 on 2023-09-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmanager', '0002_banermodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('address', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
