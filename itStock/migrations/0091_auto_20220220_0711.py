# Generated by Django 3.2.5 on 2022-02-20 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_order_accessoriesname'),
        ('itStock', '0090_auto_20220220_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorydetail',
            name='GraphicsCard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='GraphicsCard', to='dashboard.category'),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='RAM2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RAM2', to='dashboard.category'),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='STORAGE2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='M2', to='dashboard.category'),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='remarks',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
