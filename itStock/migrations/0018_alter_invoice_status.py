# Generated by Django 3.2.5 on 2021-09-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0017_auto_20210922_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], default='SEND', max_length=10, null=True),
        ),
    ]
