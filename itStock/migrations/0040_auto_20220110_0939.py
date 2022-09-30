# Generated by Django 3.2.5 on 2022-01-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0039_alter_invoice_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='pdf',
            field=models.FileField(default='invoice.pdf', upload_to='invoice_pdf'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='macaddress',
            field=models.CharField(default='00-00-00-00', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='warranty',
            field=models.CharField(choices=[('NULL', 'NULL'), ('30 D', '30 D'), ('60 D', '60 D'), ('90 D', '90 D'), ('1 Year', '1 Year'), ('2 Year', '2 Year'), ('3 Year', '3 Year'), ('Life Time', 'Life Time')], max_length=10, null=True),
        ),
    ]
