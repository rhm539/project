# Generated by Django 3.2.5 on 2022-02-07 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20220207_0607'),
        ('itStock', '0055_invoicedetail_addstock'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicedetail',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.category'),
        ),
    ]
