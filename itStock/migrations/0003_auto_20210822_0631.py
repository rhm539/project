# Generated by Django 3.2.5 on 2021-08-22 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0002_funddetail_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funddetail',
            old_name='test',
            new_name='fubdSerial',
        ),
        migrations.RemoveField(
            model_name='funddetail',
            name='fundNumber',
        ),
    ]
