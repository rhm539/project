# Generated by Django 3.2.5 on 2022-02-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0064_funddetail_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]