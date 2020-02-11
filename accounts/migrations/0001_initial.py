# Generated by Django 2.2.4 on 2020-02-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(max_length=255)),
                ('http_inner', models.CharField(max_length=255)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('show_only_when', models.IntegerField(blank=True, choices=[(0, 'Not Authenticated'), (1, 'Authenticated')], null=True)),
            ],
        ),
    ]
