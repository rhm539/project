# Generated by Django 3.2.5 on 2022-02-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0091_auto_20220220_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorydetail',
            name='Laptopbag',
            field=models.BooleanField(default=False),
        ),
    ]
