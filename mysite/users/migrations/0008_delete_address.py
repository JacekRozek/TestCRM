# Generated by Django 4.1.3 on 2023-01-19 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_person_nip_remove_person_pesel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
