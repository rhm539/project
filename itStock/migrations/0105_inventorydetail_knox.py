# Generated by Django 3.2.5 on 2022-02-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0104_alter_inventorydetail_mobilemacc'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorydetail',
            name='Knox',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=10, null=True),
        ),
    ]
