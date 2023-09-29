# Generated by Django 3.0 on 2023-09-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_problem_req_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='patients',
            field=models.ManyToManyField(related_name='doctors', to='hospital.PatientProfile'),
        ),
    ]
