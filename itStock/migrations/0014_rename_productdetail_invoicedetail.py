# Generated by Django 3.2.5 on 2021-09-22 11:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_order_orderserial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itStock', '0013_productdetail_unitprice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductDetail',
            new_name='InvoiceDetail',
        ),
    ]