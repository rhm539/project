# Generated by Django 3.2.5 on 2022-02-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_order_orderserial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='quantity',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('STOCK', 'STOCK'), ('DAMAGE', 'DAMAGE')], default='ACTIVE', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('STOCK', 'STOCK'), ('DAMAGE', 'DAMAGE')], default='ACTIVE', max_length=10, null=True),
        ),
    ]
