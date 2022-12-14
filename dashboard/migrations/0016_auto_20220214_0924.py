# Generated by Django 3.2.5 on 2022-02-14 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0015_alter_order_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrStatus',
            field=models.CharField(choices=[('NEW', 'NEW'), ('SEND', 'SEND')], default='NEW', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
