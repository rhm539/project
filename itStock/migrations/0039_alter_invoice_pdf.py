# Generated by Django 3.2.5 on 2022-01-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0038_alter_invoice_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='pdf',
            field=models.FileField(blank=True, default='invoice.pdf', upload_to='invoice_pdf'),
        ),
    ]
