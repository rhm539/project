# Generated by Django 3.2.5 on 2022-01-05 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0029_invoicedetail_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicedetail',
            name='image',
        ),
    ]
