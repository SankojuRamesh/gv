# Generated by Django 3.2.20 on 2023-09-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanager', '0004_ordermodel_orderby'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='orderquentity',
            field=models.IntegerField(default=0),
        ),
    ]
