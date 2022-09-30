# Generated by Django 3.2.5 on 2022-02-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0101_inventoryall'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorydetail',
            name='MobileBrand',
            field=models.CharField(choices=[('HP', 'HP'), ('DELL', 'DELL'), ('LENOVO', 'LENOVO'), ('MAC', 'MAC'), ('ACER', 'ACER')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='inventorydetail',
            name='MobileMacc',
            field=models.CharField(default='00-00-00-00', max_length=150, null=True),
        ),
    ]