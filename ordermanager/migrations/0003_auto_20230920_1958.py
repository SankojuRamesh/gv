# Generated by Django 3.2.20 on 2023-09-20 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanager', '0002_auto_20230920_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='orderby',
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='orderid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='orderprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
