# Generated by Django 4.0.4 on 2022-06-03 07:04

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('credits', models.PositiveIntegerField(default=100)),
                ('linkedin_token', models.TextField(blank=True, default='')),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]