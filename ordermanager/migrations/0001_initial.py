# Generated by Django 3.2.20 on 2023-09-20 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productmanager', '0002_auto_20230906_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=200)),
                ('orderprice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('orderdate', models.DateTimeField(auto_now_add=True)),
                ('paymentid', models.CharField(blank=True, max_length=200, null=True)),
                ('paymentmethod', models.CharField(blank=True, max_length=200, null=True)),
                ('shippingid', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(default='', max_length=254)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=254, null=True)),
                ('provider_order_id', models.CharField(max_length=40)),
                ('payment_id', models.CharField(max_length=36)),
                ('signature_id', models.CharField(max_length=128)),
                ('orderby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanager.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productQuntity', models.IntegerField(blank=True, null=True)),
                ('shipping_state', models.CharField(choices=[('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('RETURNED', 'Returned')], default='PENDING', max_length=50)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordermanager.ordermodel')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='productmanager.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productmanager.productmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
