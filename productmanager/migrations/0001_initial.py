# Generated by Django 3.2.20 on 2023-09-02 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorymanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('property', models.CharField(max_length=50)),
                ('coverImage', models.ImageField(upload_to='products')),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='products')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='products')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='products')),
                ('Image4', models.ImageField(blank=True, null=True, upload_to='products')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorymanager.subcategorymodel')),
            ],
        ),
    ]