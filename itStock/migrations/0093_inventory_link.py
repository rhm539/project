# Generated by Django 3.2.5 on 2022-02-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0092_inventorydetail_laptopbag'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='link',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
