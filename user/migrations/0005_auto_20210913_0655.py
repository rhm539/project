# Generated by Django 3.2.5 on 2021-09-13 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_depthead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='pdefault.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='signature',
            field=models.ImageField(default='sdefault.png', upload_to='signature_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='utype',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='user.usertype'),
        ),
    ]
