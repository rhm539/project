# Generated by Django 3.2.5 on 2022-02-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0086_auto_20220220_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorydetail',
            name='remarks',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
