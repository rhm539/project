# Generated by Django 3.2.5 on 2022-02-16 07:02

from django.db import migrations, models
import itStock.models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0077_auto_20220216_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorypc',
            name='inventoryNumber',
            field=models.CharField(default=itStock.models.increment_Inventory_number, editable=False, max_length=150, unique=True),
        ),
    ]
