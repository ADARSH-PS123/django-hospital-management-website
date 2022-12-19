# Generated by Django 4.1.2 on 2022-12-13 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='doctors')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.departments')),
            ],
        ),
    ]
