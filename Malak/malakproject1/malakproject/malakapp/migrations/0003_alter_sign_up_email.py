# Generated by Django 4.0.4 on 2022-05-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malakapp', '0002_forgot_password_sign_in_alter_sign_up_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='Email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]