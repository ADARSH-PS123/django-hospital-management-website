# Generated by Django 4.1.2 on 2022-12-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_appointments_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
