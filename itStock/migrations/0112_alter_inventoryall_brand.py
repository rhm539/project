# Generated by Django 3.2.5 on 2022-02-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0111_alter_inventoryall_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryall',
            name='Brand',
            field=models.CharField(choices=[('HP', 'HP'), ('DELL', 'DELL'), ('LENOVO', 'LENOVO'), ('MAC', 'MAC'), ('ACER', 'ACER')], max_length=30, null=True),
        ),
    ]
