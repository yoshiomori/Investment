# Generated by Django 2.2.4 on 2020-05-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_asset_hide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
