# Generated by Django 4.1.3 on 2023-01-18 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesel', models.CharField(max_length=11, null=True)),
                ('first_name', models.CharField(default='', max_length=40)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('birth_date', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('F', 'Kobieta'), ('M', 'Mężczyzna')], max_length=1, null=True)),
                ('client', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.client')),
            ],
        ),
        migrations.CreateModel(
            name='Telephone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.person')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField(auto_now=True)),
                ('fire_date', models.DateField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.person')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=10)),
                ('apartmentNumber', models.CharField(max_length=5)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.person')),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
