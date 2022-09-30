# Generated by Django 3.2.5 on 2022-02-16 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_alter_order_orstatus'),
        ('itStock', '0074_auto_20220216_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorypc',
            name='quantity',
        ),
        migrations.AddField(
            model_name='inventorypc',
            name='Processor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category'),
        ),
    ]