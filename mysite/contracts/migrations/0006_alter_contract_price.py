# Generated by Django 4.1.3 on 2023-01-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_alter_contract_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='price',
            field=models.IntegerField(help_text='USD'),
        ),
    ]
