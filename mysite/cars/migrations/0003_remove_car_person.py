# Generated by Django 4.1.3 on 2023-01-18 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='person',
        ),
    ]