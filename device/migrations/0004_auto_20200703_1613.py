# Generated by Django 3.0.7 on 2020-07-03 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0003_auto_20200703_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motor',
            old_name='Capacity',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='motor',
            old_name='Controller',
            new_name='controller',
        ),
        migrations.RenameField(
            model_name='motor',
            old_name='Fuel',
            new_name='fuel',
        ),
        migrations.RenameField(
            model_name='motor',
            old_name='Type',
            new_name='operation',
        ),
        migrations.RenameField(
            model_name='motor',
            old_name='Power',
            new_name='power',
        ),
    ]
