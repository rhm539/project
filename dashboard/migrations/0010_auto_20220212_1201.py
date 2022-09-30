# Generated by Django 3.2.5 on 2022-02-12 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20220207_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('STOCK', 'STOCK'), ('DAMAGE', 'DAMAGE')], default='ACTIVE', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('STOCK', 'STOCK'), ('DAMAGE', 'DAMAGE')], default='ACTIVE', max_length=10, null=True),
        ),
    ]
