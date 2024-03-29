# Generated by Django 2.2.6 on 2019-11-01 19:51

import django.db.models.deletion
import djongo.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('number', models.CharField(default='Unknown', max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('consultant',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(blank=True, max_length=500)),
                ('quantity', models.IntegerField()),
                ('optional_description', models.CharField(blank=True, max_length=100)),
                ('price', models.BigIntegerField(default=0)),
                ('consultant',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLog',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('consultant',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer',
                 models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   to='inventory.Customers')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Products')),
            ],
        ),
    ]
