# Generated by Django 3.0 on 2023-09-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20230910_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='dgr',
            field=models.CharField(choices=[('k', 'select your Gender'), ('M', 'Male'), ('F', 'Female')], default='k', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='dspecialites',
            field=models.CharField(choices=[('G', '----Select Specialites----'), ('General Medicine', 'General Medicine'), ('Urology & Andrology', 'Urology & Andrology'), ('Neurology', 'Neurology'), ('Orthopaedics', 'Orthopaedics'), ('Cardiology', 'Cardiology'), ('Stomach', 'Stomach'), ('ENT', 'ENT')], default='G', max_length=50),
        ),
        migrations.AlterField(
            model_name='problem',
            name='prob',
            field=models.CharField(choices=[('P', 'select your problem'), ('Orthopaedics', 'leg and Hand pain'), ('Orthopaedics', 'neck and Back pain'), ('Cardiology', 'chest pain'), ('Neurology', 'head pain'), ('Stomach', 'stomach pain'), ('ENT', 'cough and cold and ear'), ('General Medicine', 'others')], default='P', max_length=50),
        ),
    ]