# Generated by Django 3.2.5 on 2021-09-11 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_dptheadname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeptHead',
        ),
    ]
