# Generated by Django 4.1.1 on 2022-09-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_alter_students_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('Other', 'Other'), ('Female', 'Female'), ('Male', 'Male')], default='other', max_length=10),
        ),
    ]
