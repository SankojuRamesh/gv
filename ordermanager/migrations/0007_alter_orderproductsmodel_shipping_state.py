# Generated by Django 3.2.20 on 2023-09-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanager', '0006_alter_orderproductsmodel_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproductsmodel',
            name='shipping_state',
            field=models.CharField(choices=[('SHIPPED', 'Dispatched'), ('DELIVERED', 'Delivered'), ('RETURNED', 'Returned'), ('CANCELED', 'Canceled')], default='PENDING', max_length=50),
        ),
    ]
