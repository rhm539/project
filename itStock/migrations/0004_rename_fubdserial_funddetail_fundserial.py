# Generated by Django 3.2.5 on 2021-08-22 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0003_auto_20210822_0631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funddetail',
            old_name='fubdSerial',
            new_name='fundSerial',
        ),
    ]
