# Generated by Django 3.2.5 on 2022-02-20 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_order_accessoriesname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=150, null=True),
        ),
    ]