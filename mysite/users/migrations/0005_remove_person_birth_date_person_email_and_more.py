# Generated by Django 4.1.3 on 2023-01-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_department_options_alter_person_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='department',
            name='location',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
