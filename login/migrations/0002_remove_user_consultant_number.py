# Generated by Django 2.1.2 on 2019-10-29 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='consultant_number',
        ),
    ]
