# Generated by Django 3.2.5 on 2021-09-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itStock', '0008_auto_20210825_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='admindpt',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fund',
            name='director',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fund',
            name='gmacc',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fund',
            name='headdept',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='fund',
            name='md',
            field=models.CharField(max_length=150, null=True),
        ),
    ]