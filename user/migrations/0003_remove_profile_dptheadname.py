# Generated by Django 3.2.5 on 2021-09-11 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_department_dptheadname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='dptHeadName',
        ),
    ]