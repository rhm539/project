# Generated by Django 3.2.5 on 2022-01-05 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0027_auto_20220105_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicedetail',
            name='image',
        ),
    ]
