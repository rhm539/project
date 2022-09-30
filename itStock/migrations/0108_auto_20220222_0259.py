# Generated by Django 3.2.5 on 2022-02-22 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0107_auto_20220222_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MobileName', models.CharField(max_length=150, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='MobileBrand',
            field=models.CharField(choices=[('SAMSUNG A32', 'SAMSUNG J6'), ('SAMSUNG J6', 'SAMSUNG J6'), ('SAMSUNG J7', 'SAMSUNG J7'), ('SAMSUNG J4', 'SAMSUNG J4'), ('iPHONE', 'iPHONE'), ('iPAD', 'iPAD'), ('PAD', 'PAD')], max_length=30, null=True),
        ),
    ]
