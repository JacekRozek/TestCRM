# Generated by Django 4.1.3 on 2023-01-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_person_birth_date_person_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nip',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='pesel',
            field=models.CharField(default='', max_length=11),
        ),
    ]
