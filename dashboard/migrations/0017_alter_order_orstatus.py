# Generated by Django 3.2.5 on 2022-02-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20220214_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrStatus',
            field=models.CharField(choices=[('NEW', 'NEW'), ('SEND', 'SEND'), ('DELIVER', 'DELIVER')], default='NEW', max_length=10, null=True),
        ),
    ]
