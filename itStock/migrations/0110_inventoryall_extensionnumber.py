# Generated by Django 3.2.5 on 2022-02-22 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0109_alter_inventorydetail_mobilebrand'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryall',
            name='ExtensionNumber',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
