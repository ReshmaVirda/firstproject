# Generated by Django 4.0.4 on 2022-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=50),
        ),
    ]
