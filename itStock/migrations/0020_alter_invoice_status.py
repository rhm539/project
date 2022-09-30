# Generated by Django 3.2.5 on 2021-09-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0019_rename_productname_invoicedetail_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], default='UNPAID', max_length=10, null=True),
        ),
    ]